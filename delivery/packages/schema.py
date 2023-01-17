import graphene
from graphene_django import DjangoObjectType
from .models import City, DeliveryMan, Package



class PackageType(DjangoObjectType):
    class Meta: 
        model = Package
        fields = ('id','title','city')

class CityType(DjangoObjectType):
    class Meta: 
        model = City
        fields = ('id','name')

class DeliveryManType(DjangoObjectType):
    class Meta: 
        model = DeliveryMan
        fields = ('id','first_name','last_name','city')



class CreatePackage(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        city = graphene.Int()

    package = graphene.Field(PackageType)

    @classmethod
    def mutate(cls, root, info, title, city):
        package = Package(title=title)
        city = City.objects.get(id=city)

        package.city = city
        package.save()
        
        return CreatePackage(package=package)


class CreateDeliveryMan(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        city = graphene.Int()

    deliveryMan = graphene.Field(DeliveryManType)

    @classmethod
    def mutate(cls, root, info, first_name,last_name, city):
        deliveryMan = DeliveryMan(first_name=first_name,last_name=last_name)
        city = City.objects.get(id=city)

        deliveryMan.city = city
        deliveryMan.save()
        
        return CreateDeliveryMan(deliveryMan=deliveryMan)


class CreateCity(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    city = graphene.Field(CityType)

    @classmethod
    def mutate(cls, root, info, name):
        city = City()
        city.name = name
        city.save()
        
        return CreateCity(city=city)

class CityInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    
class UpdateCity(graphene.Mutation):
    class Arguments:
        city_data = CityInput(required=True)


    city = graphene.Field(CityType)
    
    @staticmethod
    def mutate(self, info,city_data=None):
        city_instance = City.objects.get(pk=city_data.id)

        print(f" city , {city_instance}")
        city_instance.name = city_data.name
        city_instance.save()
        return UpdateCity(city=city_instance)

class DeleteCity(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    city = graphene.Field(CityType)

    @staticmethod
    def mutate(root, info, id):
        city_instance = City.objects.get(pk=id)
        city_instance.delete()

        return None
    
class Mutation(graphene.ObjectType):
    create_package = CreatePackage.Field()
    create_deliveryMan = CreateDeliveryMan.Field()
    create_city = CreateCity.Field()
    update_city = UpdateCity.Field()
    delete_city = DeleteCity.Field()

class Query(graphene.ObjectType):
    city = graphene.List(CityType)
    city_by_id = graphene.Field(CityType, id=graphene.Int())
    package = graphene.List(PackageType)
    DeliveryMan = graphene.List(DeliveryManType)

    def resolve_city(root, info):
        return City.objects.all()

    def resolve_city_by_id(root, info, id):
        return City.objects.get(pk=id)

    def resolve_package(root, info):
        return Package.objects.all()

    def resolve_devliveryMan(root, info):
        return DeliveryMan.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)
