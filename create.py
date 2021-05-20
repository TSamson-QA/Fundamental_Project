from app import db, Models, Paints

db.drop_all()
db.create_all()

MacBlue = Paints(paint_name = "Macragge Blue", needed=0)
db.session.add(MacBlue)

WBGreen = Paints(paint_name = "Warboss Green", needed=0)
db.session.add(WBGreen)

MRed = Paints(paint_name = "Mephiston Red", needed=0)
db.session.add(MRed)

ABlack = Paints(paint_name = "Abbadon Black", needed=0)
db.session.add(ABlack)

AEarthshade = Paints(paint_name = "Agrax Earthshade", needed=0)
db.session.add(AEarthshade)

White = Paints(paint_name = "White Scar", needed=0)
db.session.add(White)

IronGrey = Paints(paint_name = "Ironbreaker", needed=0)
db.session.add(IronGrey)

AvSunset = Paints(paint_name = "Averland Sunset", needed=0)
db.session.add(AvSunset)

db.session.commit()

UM = Models(model_name="Ultramarines", Paints = MacBlue)
db.session.add(UM)
Orks = Models(model_name="Orks", Paints = WBGreen)
db.session.add(Orks)
BA = Models(model_name="Blood Angels", Paints = MRed)
db.session.add(BA)
BT = Models(model_name="Black Templars", Paints = ABlack)
db.session.add(BT)
Necrons = Models(model_name="Necrons", Paints = AEarthshade)
db.session.add(Necrons)
Tau = Models(model_name="Tau", Paints = White)
db.session.add(Tau)
GrK = Models(model_name="Grey Knights", Paints = IronGrey)
db.session.add(GrK)
ImF = Models(model_name="Imperial Fists", Paints = AvSunset)
db.session.add(ImF)

db.session.commit()

