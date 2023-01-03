from abs_pth import filenames, root_path
from app.data.data_types import Gender, Verification
from app.data import models
from config.config import settings as env
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f"postgresql://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@" \
               f"{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}/{env.DATABASE_NAME}"
gen = {"F": Gender.female,
       "M": Gender.male,
       "Zh": Gender.female,
       "female": Gender.female,
       "male": Gender.male,
       "Female": Gender.female,
       "Male": Gender.male}

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
data = Session()
Base = declarative_base()
# URL = "https://adoption.com/baby-names/origin/French?page="
# for loop in range(0, 32):
#     NEW_URL = URL + str(loop + 1)
#     webs = requests.get(NEW_URL)
#     soup = BeautifulSoup(webs.content)
#     name = soup.find_all("td", class_="text-wrap")[::4]
#     gender = soup.find_all("td", class_="d-none d-sm-table-cell")
#     for person, sex in zip(name, gender):
#         if sex.text not in gen.keys():
#             pass
#
#         else:
#             instance = data.query(models.Names).filter(
#                 models.Names.name == person.text,
#                 models.Names.gender == gen[sex.text],
#                 models.Names.country == Country.french
#             ).first()
#             if instance:
#                 pass
#
#             else:
#
#                 new_data = models.Names(
#                     name=person.text,
#                     gender=gen[sex.text],
#                     country=Country.french,
#                     verification=Verification.valid
#
#                 )
#                 data.add(new_data)
#                 data.commit()
#
# data.close()
#
#
#
#
#
#

WHERE = ["app", "data", "public_data"]
txt_name = filenames(where=WHERE)
txt_name.sort()
for txt in txt_name:
    txt = root_path(where=["app", "data", "public_data", txt])
    file = open(txt, "r")
    data_list = file.read()
    name_list = data_list.split("\n")

    for person in name_list:
        name = person.split(",")[0]
        gender = person.split(",")[1]
        country = person.split(",")[2]

        if name != "name" and name != "":

            instance = data.query(models.Names).filter(
                models.Names.name == name,
                models.Names.gender == gender,
                models.Names.country == country
            ).first()

            if instance:
                pass

            else:
                new_data = models.Names(
                    name=name,
                    gender=gender,
                    country=country,
                    verification=Verification.unknown
                )
                data.add(new_data)
                data.commit()

data.close()
