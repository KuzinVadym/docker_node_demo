import { MongoClient } from 'mongodb';

import settings from '../settings'

class Database {
   constructor() {
     this.db;
   }
   set(db) { this.db = db; };
   get() { return this.db; };
   init() {
     MongoClient.connect(`${settings.get('db_path')}/${settings.get('db_name')}`, (err, db) => {
       if (err) console.log(err);
       console.log("Mongo Client conected");
       this.db = db.db(settings.get('db_name'))
     });
   }
   close() { this.db.close(); };
}

export default new Database();