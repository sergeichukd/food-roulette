# food-roulette

init migrations:
```bash
alembic init migrations
```

go to `alembic.ini` and setup sqlite like show below:
```
sqlalchemy.url = sqlite:///data.db
```

Make migrations like in [this post](https://kimsereylam.com/sqlalchemy/2019/10/18/get-started-with-alembic.html)


