from graphene import ObjectType, String, Int, Interface, Mutation, List, Field
from graphene_federation import build_schema, key

class ProductInterface(Interface):
    id = Int(required=True)
    body = String(required=True)

@key(fields='id') # Внешний ключ ( а-ля primary key )
class Product(ObjectType):
    class Meta:
        interfaces = (ProductInterface,)

    # метод для получения данных по внешнему ключу
    def __resolve_reference(self, info, **kwargs):
        return Product(id=self.id, body=f'funny_text_{self.id}')

@key('id')
@key('email')
class User(ObjectType):
    id = Int(required=True)
    email = String()
    age = Int()

    # резолвер для конкретного поля
    def resolve_age(self, info):
        return 24

    def __resolve_reference(self, info, **kwargs):
        if self.id is not None:
            return User(id=self.id, email=f'name_{self.id}@gmail.com')

        return User(id=123, email=self.email)

class Query(ObjectType):
    all_products = List(Product)
    all_users = List(User)

    def resolve_all_products(self, info):
        # Fetch and return all products from your database
        # For now, I will return some mock data
        return [
            Product(id=1, body="Product 1"),
            Product(id=2, body="Product 2")
        ]

    def resolve_all_users(self, info):
        # Fetch and return all users from your database
        # For now, I will return some mock data
        return [
            User(id=1, email="user1@gmail.com"),
            User(id=2, email="user2@gmail.com")
        ]
class CreateUser(Mutation):
    class Arguments:
        id = Int(required=True)
        email = String(required=True)

    Output = User

    def mutate(root, info, id, email):
        # You should persist these details here
        return User(id=id, email=email)

class CreateProduct(Mutation):
    class Arguments:
        id = Int(required=True)
        body = String(required=True)

    Output = Product

    def mutate(root, info, id, body):
        # You should persist these details here
        return Product(id=id, body=body)

class Mutation(ObjectType):
    create_user = CreateUser.Field()
    create_product = CreateProduct.Field()

types = [
    Product,
    User
]

schema = build_schema(query=Query, mutation=Mutation, types=types)