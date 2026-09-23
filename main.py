from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)



class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    category: str
    location: str
    reported_by: str
    status: str

def create_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI(
    title="College Lost & Found API"
)


@app.on_event("startup")
def startup():
    create_tables()


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):

    if not item.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title must not be empty"
        )

    if len(item.description.strip()) < 5:
        raise HTTPException(
            status_code=400,
            detail="Description must contain meaningful text"
        )

    if item.status not in ["Lost", "Found", "Returned"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be Lost, Found, or Returned"
        )

    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)

        return item


@app.get("/items", response_model=list[Item])
def get_items():

    with Session(engine) as session:
        statement = select(Item)
        items = session.exec(statement).all()

        return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):

    with Session(engine) as session:

        item = session.get(Item, item_id)

        if item is None:
            raise HTTPException(
                status_code=404,
                detail="Item not found"
            )

        return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):

    if not updated_item.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title must not be empty"
        )

    if len(updated_item.description.strip()) < 5:
        raise HTTPException(
            status_code=400,
            detail="Description must contain meaningful text"
        )

    if updated_item.status not in ["Lost", "Found", "Returned"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be Lost, Found, or Returned"
        )

    with Session(engine) as session:

        item = session.get(Item, item_id)

        if item is None:
            raise HTTPException(
                status_code=404,
                detail="Item not found"
            )

        item.title = updated_item.title
        item.description = updated_item.description
        item.category = updated_item.category
        item.location = updated_item.location
        item.reported_by = updated_item.reported_by
        item.status = updated_item.status

        session.commit()
        session.refresh(item)

        return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):

    with Session(engine) as session:

        item = session.get(Item, item_id)

        if item is None:
            raise HTTPException(
                status_code=404,
                detail="Item not found"
            )

        session.delete(item)
        session.commit()

        return {
            "message": "Item deleted successfully",
            "item_id": item_id
        }



@app.get("/items/status/{status}", response_model=list[Item])
def get_items_by_status(status: str):

    if status not in ["Lost", "Found", "Returned"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be Lost, Found, or Returned"
        )

    with Session(engine) as session:

        statement = select(Item).where(Item.status == status)
        items = session.exec(statement).all()

        return items


@app.get("/items/category/{category}", response_model=list[Item])
def get_items_by_category(category: str):

    with Session(engine) as session:

        statement = select(Item).where(Item.category == category)
        items = session.exec(statement).all()

        return items