import datetime


class Weather:

    all_weather = []

    def __init__(self,data):
        self.id = data['id']
        self.city=data['city']
        self.state=data['state']
        self.temp=data['temp']
        self.precip = data['precip']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls,data):
        id = len(cls.all_weather) + 1
        
        data["id"] = id
        data['created_at'] = datetime.datetime.now()
        data['updated_at']= datetime.datetime.now()
        cls.all_weather.append(cls(data))
        return cls.all_weather[len(cls.all_weather)-1].id
    @classmethod
    def get_all(cls):
        return cls.all_weather
    @classmethod
    def get_one_by_id(cls,id):
    
        for item in cls.all_weather:
            if item.id == id:
                return item
        return []
    @classmethod
    def get_one_by_city(cls,city):
        
        for item in cls.all_weather:
            if item.city == city:
                return item
        return []
    def __repr__(self):
        return f"{{'id':{self.id},'city':{self.city},'state':{self.state},'temp':{self.temp},'precip':{self.precip},'created_at':{self.created_at},'updated_at':{self.updated_at}}}"
