# food-roulette


## How to use alembic
init migrations:
```bash
alembic init migrations
```

go to `alembic.ini` and setup sqlite like show below:
```
sqlalchemy.url = sqlite:///data.db
```

Make migrations like in [this post](https://kimsereylam.com/sqlalchemy/2019/10/18/get-started-with-alembic.html)

Init migraitons:
```bash
alembic init migrations
```

Create new migration
```bash
alembic revision -m "create user table"
```

On upgrade we create a table user with three columns and on downgrade we drop the table. We can then first check where our database state is at with `alembic current`:
```bash
$ alembic current
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
```

The first line indicates that Alembic understands that the url we provided targets SQLite. Then we can look at the history
```bash
$ alembic history
<base> -> d6695a405895 (head), create user table
```

We see that we have one migration pending d6695a405895 where head points to. We can then upgrade using upgrade head to upgrade to the latest revision:
```bash
$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> d6695a405895, create user table

```

After running the migration, we can see current
```bash
$ alembic current
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
d6695a405895 (head)
```

To downgrade the revision –
```bash
alembic downgrade -1
# or
alembic downgrade ed34c6h4896k
```
