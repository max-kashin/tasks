import sqlalchemy


metadata = sqlalchemy.MetaData()

# association_table = sqlalchemy.Table('association', sqlalchemy.Base.metadata,
#     sqlalchemy.Column('left_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('left.id')),
#     sqlalchemy.Column('right_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('right.id'))
# )

persons_table = sqlalchemy.Table(
    "persons",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(100)),
    sqlalchemy.Column("event", sqlalchemy.ForeignKey("users.id")),
)


events_table = sqlalchemy.Table(
    "events",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("date", sqlalchemy.DateTime()),
    sqlalchemy.Column("description", sqlalchemy.String(1000)),
)

