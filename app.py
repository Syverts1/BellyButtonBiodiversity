# import necessary libraries
from sqlalchemy import func
import numpy as np
import pandas as pd
import json

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///belly_button_biodiversity.sqlite"

db = SQLAlchemy(app)

class Otu(db.Model):
    __tablename__ = 'otu'

    otu_id = db.Column(db.Integer, primary_key=True)
    lowest_taxonomic_unit_found = db.Column(db.String)

    def __repr__(self):
        return '<Emoji %r>' % (self.name)

class Metadata(db.Model):
    __tablename__ = 'samples_metadata'
    
    SAMPLEID =db.Column(db.Integer, primary_key=True)
    EVENT = db.Column(db.String)
    ETHNICITY = db.Column(db.String)
    GENDER = db.Column(db.String)
    AGE = db.Column(db.Integer)
    WFREQ = db.Column(db.Integer) 
    BBTYPE = db.Column(db.String) 
    LOCATION = db.Column(db.String)
    COUNTRY012 = db.Column(db.String) 
    ZIP012 = db.Column(db.Integer) 
    COUNTRY1319 = db.Column(db.String) 
    ZIP1319 = db.Column(db.Integer) 
    DOG = db.Column(db.String) 
    CAT = db.Column(db.String) 
    IMPSURFACE013 = db.Column(db.Integer) 
    NPP013 = db.Column(db.Float) 
    MMAXTEMP013 = db.Column(db.Float)
    PFC013 = db.Column(db.Float)
    IMPSURFACE1319 = db.Column(db.Integer) 
    NPP1319 = db.Column(db.Float)
    MMAXTEMP1319 = db.Column(db.Float) 
    PFC1319 = db.Column(db.Float)

    def __repr__(self):
        return '<Emoji %r>' % (self.name)

class Samples(db.Model):
    __tablename__ = 'samples'
    
    otu_id =db.Column(db.Integer, primary_key=True)
    BB_940 =db.Column(db.Integer)
    BB_941 =db.Column(db.Integer) 
    BB_943 =db.Column(db.Integer) 
    BB_944 =db.Column(db.Integer) 
    BB_945 =db.Column(db.Integer) 
    BB_946 =db.Column(db.Integer) 
    BB_947 =db.Column(db.Integer) 
    BB_948 =db.Column(db.Integer) 
    BB_949 =db.Column(db.Integer) 
    BB_950 =db.Column(db.Integer) 
    BB_952 =db.Column(db.Integer) 
    BB_953 =db.Column(db.Integer) 
    BB_954 =db.Column(db.Integer) 
    BB_955 =db.Column(db.Integer) 
    BB_956 =db.Column(db.Integer) 
    BB_958 =db.Column(db.Integer) 
    BB_959 =db.Column(db.Integer) 
    BB_960 =db.Column(db.Integer) 
    BB_961 =db.Column(db.Integer) 
    BB_962 =db.Column(db.Integer) 
    BB_963 =db.Column(db.Integer) 
    BB_964 =db.Column(db.Integer) 
    BB_966 =db.Column(db.Integer) 
    BB_967 =db.Column(db.Integer) 
    BB_968 =db.Column(db.Integer) 
    BB_969 =db.Column(db.Integer) 
    BB_970 =db.Column(db.Integer) 
    BB_971 =db.Column(db.Integer) 
    BB_972 =db.Column(db.Integer) 
    BB_973 =db.Column(db.Integer) 
    BB_974 =db.Column(db.Integer) 
    BB_975 =db.Column(db.Integer) 
    BB_978 =db.Column(db.Integer) 
    BB_1233 =db.Column(db.Integer) 
    BB_1234 =db.Column(db.Integer) 
    BB_1235 =db.Column(db.Integer) 
    BB_1236 =db.Column(db.Integer) 
    BB_1237 =db.Column(db.Integer) 
    BB_1238 =db.Column(db.Integer) 
    BB_1242 =db.Column(db.Integer) 
    BB_1243 =db.Column(db.Integer) 
    BB_1246 =db.Column(db.Integer) 
    BB_1253 =db.Column(db.Integer) 
    BB_1254 =db.Column(db.Integer) 
    BB_1258 =db.Column(db.Integer) 
    BB_1259 =db.Column(db.Integer) 
    BB_1260 =db.Column(db.Integer) 
    BB_1264 =db.Column(db.Integer) 
    BB_1265 =db.Column(db.Integer) 
    BB_1273 =db.Column(db.Integer) 
    BB_1275 =db.Column(db.Integer) 
    BB_1276 =db.Column(db.Integer) 
    BB_1277 =db.Column(db.Integer) 
    BB_1278 =db.Column(db.Integer) 
    BB_1279 =db.Column(db.Integer) 
    BB_1280 =db.Column(db.Integer) 
    BB_1281 =db.Column(db.Integer) 
    BB_1282 =db.Column(db.Integer) 
    BB_1283 =db.Column(db.Integer) 
    BB_1284 =db.Column(db.Integer) 
    BB_1285 =db.Column(db.Integer) 
    BB_1286 =db.Column(db.Integer) 
    BB_1287 =db.Column(db.Integer) 
    BB_1288 =db.Column(db.Integer) 
    BB_1289 =db.Column(db.Integer) 
    BB_1290 =db.Column(db.Integer) 
    BB_1291 =db.Column(db.Integer) 
    BB_1292 =db.Column(db.Integer) 
    BB_1293 =db.Column(db.Integer) 
    BB_1294 =db.Column(db.Integer) 
    BB_1295 =db.Column(db.Integer) 
    BB_1296 =db.Column(db.Integer) 
    BB_1297 =db.Column(db.Integer) 
    BB_1298 =db.Column(db.Integer) 
    BB_1308 =db.Column(db.Integer) 
    BB_1309 =db.Column(db.Integer) 
    BB_1310 =db.Column(db.Integer) 
    BB_1374 =db.Column(db.Integer) 
    BB_1415 =db.Column(db.Integer) 
    BB_1439 =db.Column(db.Integer) 
    BB_1441 =db.Column(db.Integer) 
    BB_1443 =db.Column(db.Integer) 
    BB_1486 =db.Column(db.Integer) 
    BB_1487 =db.Column(db.Integer) 
    BB_1489 =db.Column(db.Integer) 
    BB_1490 =db.Column(db.Integer) 
    BB_1491 =db.Column(db.Integer) 
    BB_1494 =db.Column(db.Integer) 
    BB_1495 =db.Column(db.Integer) 
    BB_1497 =db.Column(db.Integer) 
    BB_1499 =db.Column(db.Integer) 
    BB_1500 =db.Column(db.Integer) 
    BB_1501 =db.Column(db.Integer) 
    BB_1502 =db.Column(db.Integer) 
    BB_1503 =db.Column(db.Integer) 
    BB_1504 =db.Column(db.Integer) 
    BB_1505 =db.Column(db.Integer) 
    BB_1506 =db.Column(db.Integer) 
    BB_1507 =db.Column(db.Integer) 
    BB_1508 =db.Column(db.Integer) 
    BB_1510 =db.Column(db.Integer) 
    BB_1511 =db.Column(db.Integer) 
    BB_1512 =db.Column(db.Integer) 
    BB_1513 =db.Column(db.Integer) 
    BB_1514 =db.Column(db.Integer) 
    BB_1515 =db.Column(db.Integer) 
    BB_1516 =db.Column(db.Integer) 
    BB_1517 =db.Column(db.Integer) 
    BB_1518 =db.Column(db.Integer) 
    BB_1519 =db.Column(db.Integer) 
    BB_1521 =db.Column(db.Integer) 
    BB_1524 =db.Column(db.Integer) 
    BB_1526 =db.Column(db.Integer) 
    BB_1527 =db.Column(db.Integer) 
    BB_1530 =db.Column(db.Integer) 
    BB_1531 =db.Column(db.Integer) 
    BB_1532 =db.Column(db.Integer) 
    BB_1533 =db.Column(db.Integer) 
    BB_1534 =db.Column(db.Integer) 
    BB_1535 =db.Column(db.Integer) 
    BB_1536 =db.Column(db.Integer) 
    BB_1537 =db.Column(db.Integer) 
    BB_1539 =db.Column(db.Integer) 
    BB_1540 =db.Column(db.Integer) 
    BB_1541 =db.Column(db.Integer) 
    BB_1542 =db.Column(db.Integer) 
    BB_1543 =db.Column(db.Integer) 
    BB_1544 =db.Column(db.Integer) 
    BB_1545 =db.Column(db.Integer) 
    BB_1546 =db.Column(db.Integer) 
    BB_1547 =db.Column(db.Integer) 
    BB_1548 =db.Column(db.Integer) 
    BB_1549 =db.Column(db.Integer) 
    BB_1550 =db.Column(db.Integer) 
    BB_1551 =db.Column(db.Integer) 
    BB_1552 =db.Column(db.Integer) 
    BB_1553 =db.Column(db.Integer) 
    BB_1554 =db.Column(db.Integer) 
    BB_1555 =db.Column(db.Integer) 
    BB_1556 =db.Column(db.Integer) 
    BB_1557 =db.Column(db.Integer) 
    BB_1558 =db.Column(db.Integer) 
    BB_1561 =db.Column(db.Integer) 
    BB_1562 =db.Column(db.Integer) 
    BB_1563 =db.Column(db.Integer) 
    BB_1564 =db.Column(db.Integer) 
    BB_1572 =db.Column(db.Integer) 
    BB_1573 =db.Column(db.Integer) 
    BB_1574 =db.Column(db.Integer) 
    BB_1576 =db.Column(db.Integer) 
    BB_1577 =db.Column(db.Integer) 
    BB_1581 =db.Column(db.Integer) 
    BB_1601 =db.Column(db.Integer)

    def __repr__(self):
        return '<Emoji %r>' % (self.name)

# Create database classes
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

#################################################
# Flask Routes
#################################################

# Query the database for names and send the jsonified results
@app.route("/names")
def names():
    results = db.session.query(Metadata.SAMPLEID).all()
    df = pd.DataFrame(results, columns=['otu_id'])
    df['otu_id'] = 'BB_' + df['otu_id'].astype(str)

    return jsonify(df['otu_id'].tolist())

# Query the database for OTU description and send the jsonified results
@app.route("/otu")
def otu():
    results = db.session.query(Otu.lowest_taxonomic_unit_found).all()
    df = pd.DataFrame(results, columns=['lowest_taxonomic_unit_found'])

    return jsonify(df['lowest_taxonomic_unit_found'].tolist())

@app.route('/metadata/<sample>')
def metadatasample(sample):
    
    s = sample.split('_')[1]

    #Args: Sample in the format: `BB_940`

    sel = [Metadata.AGE, Metadata.BBTYPE, Metadata.ETHNICITY, Metadata.GENDER, Metadata.LOCATION, Metadata.SAMPLEID]
    
    results = db.session.query(*sel).filter(Metadata.SAMPLEID == s).all()
    df = pd.DataFrame(results, columns=['AGE', 'BBTYPE','ETHNICITY','GENDER','LOCATION','SAMPLEID'])
    
    return jsonify(df.to_dict(orient="records"))

@app.route('/wfreq/<sample>')
def wfreq(sample):
    s = sample.split('_')[1]
    
    sel = [Metadata.WFREQ]
    
    results = db.session.query(*sel).filter(Metadata.SAMPLEID == s).all()
    
    
    return jsonify(results[0][0])

@app.route('/samples/<sample>')
def samples(sample):

    sel = [Samples.otu_id, getattr(Samples, sample)]
        
    results = db.session.query(*sel).all()
    df = pd.DataFrame(results, columns=['otu_id', 'sample_values'])

    df = df[df['sample_values'] > 0]
    df= df.sort_values(by=['sample_values'],ascending=False)

    samples_list = [{'otu_ids':df['otu_id'].tolist(),'sample_values':df['sample_values'].tolist()}]
    
    return jsonify(samples_list)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
