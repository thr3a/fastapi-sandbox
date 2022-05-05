
```
uvicorn hello_world.main:app --reload --port 3000
```

http://127.0.0.1:3000/

- Swagger http://127.0.0.1:3000/docs
- Redoc http://127.0.0.1:3000/redoc

# 階層別

- hello_world: hellow worldするだけ
- no_database: pydanticのサンプル つまりpydanticはDBに一切関わりはない
- sqlite_app1: SQLiteでUserの必要最低限のCRUD
- sqlite_app2:
  - レスポンスモデルの導入 schemas.pyが拡張されてる
    - showのときにパスワード表示しないように
  - Postモデル作成
  - usersに多数のpostsがぶら下がっている関係(relationship)
