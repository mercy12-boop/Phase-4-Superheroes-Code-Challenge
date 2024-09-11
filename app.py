# #!/usr/bin/env python3

# from flask import Flask, request, make_response, jsonify
# from flask_restful import Resource, Api
# from flask_migrate import Migrate
# from models import db, Hero, Power, HeroPower

# app = Flask(__name__)
# api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# migrate = Migrate(app, db)
# db.init_app(app)

# @app.route('/')
# def home():
#     return 'Welcome to the superheroes API'

# class Heroes(Resource):
#     def get(self):
#         heroes = []
#         for hero in Hero.query.all():
#             hero_dict = {
#                 "id": hero.id,
#                 "name": hero.name,
#                 "super_name": hero.super_name
#             }
#             heroes.append(hero_dict)
#         return make_response(jsonify(heroes), 200)

# class HeroesId(Resource):
#     def get(self, id):
#         hero = Hero.query.filter(Hero.id == id).first()
#         if hero:
#             hero_dict = {
#                 "id": hero.id,
#                 "name": hero.name,
#                 "super_name": hero.super_name,
#                 "hero_powers": []
#             }
#             for hero_power in hero.hero_power:
#                 power_dict = {
#                     "id": hero_power.power.id,
#                     "name": hero_power.power.name,
#                     "description": hero_power.power.description
#                 }
#                 hero_dict["hero_powers"].append(power_dict)
#             return make_response(jsonify(hero_dict), 200)
#         else:
#             return make_response(jsonify({"error": "Hero not found"}), 404)

# class Powers(Resource):
#     def get(self):
#         powers = []
#         for power in Power.query.all():
#             power_dict = {
#                 "id": power.id,
#                 "name": power.name,
#                 "description": power.description
#             }
#             powers.append(power_dict)
#         return make_response(jsonify(powers), 200)

# class PowersId(Resource):
#     def get(self, id):
#         power = Power.query.filter(Power.id == id).first()
#         if power:
#             power_dict = {
#                 "id": power.id,
#                 "name": power.name,
#                 "description": power.description
#             }
#             return make_response(jsonify(power_dict), 200)
#         else:
#             return make_response(jsonify({"error": "Power not found"}), 404)

#     def patch(self, id):
#         power = Power.query.filter(Power.id == id).first()
#         if not power:
#             return make_response(jsonify({"error": "Power not found"}), 404)
        
#         data = request.get_json()
#         try:
#             if 'description' in data:
#                 description = data['description']
#                 if len(description) < 20:
#                     raise ValueError ('description must be at least 20 characters')
#                 power.description = description
#             db.session.commit()
            
#             power_dict = {
#                 "id": power.id,
#                 "name": power.name,
#                 "description": power.description
#             }
#             return make_response(jsonify(power_dict), 200)
#         except ValueError as e:
#             return make_response(jsonify({"errors": [str(e)]}), 400)

# class HeroPower(Resource):
#     def post(self):
#         data = request.get_json()
#         try:
#             strength = data.get('strength')
#             if strength not in ['Strong', 'Weak', 'Average']:
#                 raise ValueError('Invalid strength value')
            
#             hero_id = data.get('hero_id')
#             power_id = data.get('power_id')

#             # Check if the hero and power exist
#             hero = Hero.query.get(hero_id)
#             power = Power.query.get(power_id)
#             if not hero or not power:
#                 raise ValueError('Hero or Power does not exist')
            
#             new_hero_power = HeroPower(
#                 strength=strength,
#                 power_id=power_id,
#                 hero_id=hero_id
#             )
#             db.session.add(new_hero_power)
#             db.session.commit()
            
#             return make_response(jsonify(new_hero_power.to_dict()), 201)
#         except ValueError as e:
#             return make_response(jsonify({"errors": [str(e)]}), 400)

# api.add_resource(Heroes, '/heroes')
# api.add_resource(HeroesId, '/heroes/<int:id>')
# api.add_resource(Powers, '/powers')
# api.add_resource(PowersId, '/powers/<int:id>')
# api.add_resource(HeroPower, '/hero_powers')

# if __name__ == '__main__':
#     app.run(debug=True, port=5555)
#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_restful import Resource, Api
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to the superheroes API'

class Heroes(Resource):
    def get(self):
        heroes = []
        for hero in Hero.query.all():
            hero_dict = {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            }
            heroes.append(hero_dict)
        return make_response(jsonify(heroes), 200)

class HeroesId(Resource):
    def get(self, id):
        hero = Hero.query.filter(Hero.id == id).first()
        if hero:
            hero_dict = {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name,
                "hero_powers": []
            }
            for hero_power in hero.hero_power:
                power_dict = {
                    "id": hero_power.power.id,
                    "name": hero_power.power.name,
                    "description": hero_power.power.description
                }
                hero_dict["hero_powers"].append(power_dict)
            return make_response(jsonify(hero_dict), 200)
        else:
            return make_response(jsonify({"error": "Hero not found"}), 404)

class Powers(Resource):
    def get(self):
        powers = []
        for power in Power.query.all():
            power_dict = {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
            powers.append(power_dict)
        return make_response(jsonify(powers), 200)

class PowersId(Resource):
    def get(self, id):
        power = Power.query.filter(Power.id == id).first()
        if power:
            power_dict = {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
            return make_response(jsonify(power_dict), 200)
        else:
            return make_response(jsonify({"error": "Power not found"}), 404)

    def patch(self, id):
        power = Power.query.filter(Power.id == id).first()
        if not power:
            return make_response(jsonify({"error": "Power not found"}), 404)

        data = request.get_json()
        try:
            if 'description' in data:
                description = data['description']
                if not isinstance(description, str) or len(description) < 20:
                    raise ValueError('description must be at least 20 characters')
                power.description = description
            db.session.commit()
            
            power_dict = {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
            return make_response(jsonify(power_dict), 200)
        except ValueError as e:
            return make_response(jsonify({"errors": [str(e)]}), 400)

class HeroPower(Resource):
    def post(self):
        data = request.get_json()
        try:
            strength = data.get('strength')
            if strength not in ['Strong', 'Weak', 'Average']:
                raise ValueError('Invalid strength value')
            
            hero_id = data.get('hero_id')
            power_id = data.get('power_id')

            # Check if the hero and power exist
            hero = Hero.query.get(hero_id)
            power = Power.query.get(power_id)
            if not hero or not power:
                raise ValueError('Hero or Power does not exist')

            new_hero_power = HeroPower(
                strength=strength,
                power_id=power_id,
                hero_id=hero_id
            )
            db.session.add(new_hero_power)
            db.session.commit()
            
            return make_response(jsonify({
                "id": new_hero_power.id,
                "strength": new_hero_power.strength,
                "hero_id": new_hero_power.hero_id,
                "power_id": new_hero_power.power_id
            }), 201)
        except ValueError as e:
            return make_response(jsonify({"errors": [str(e)]}), 400)

api.add_resource(Heroes, '/heroes')
api.add_resource(HeroesId, '/heroes/<int:id>')
api.add_resource(Powers, '/powers')
api.add_resource(PowersId, '/powers/<int:id>')
api.add_resource(HeroPower, '/hero_powers')

if __name__ == '__main__':
    app.run(debug=True, port=5555)
