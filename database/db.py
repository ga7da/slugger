from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

engine = create_async_engine(url="postgresql+asyncpg://user:password@localhost/dbname")

new_session = async_sessionmaker(bind=engine, expire_on_commit=False)
