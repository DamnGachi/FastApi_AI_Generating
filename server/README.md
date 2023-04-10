# Галерея сгенерированных AI картинок

**Make Migrations**
```
poetry run init migrations
```
```
poetry run alembic revision --autogenerate -m
```
```
poetry run alembic upgrade head
```

**Install Poetry Dependencies**
```
make install
```

**Install RabbitMQ in wsl**
```
brew install rabbitmq
```
```
brew services start rabbitmq
```
