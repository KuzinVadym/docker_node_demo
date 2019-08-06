var dev = require('./dev.json');
var prod = require('./prod.json');

class Settings {
   constructor() {
     this.set;
   }
   set(mode) {
     switch (mode) {
       case 'dev':
         console.log("You set settings with dev mode");
         return this.set = dev;
       case 'prod':
         console.log("You set settings with prod mode");
         return this.set = prod;
       default:
         console.log("You set settings with def mode");
         return this.set = dev;
     }
   };
   get(key){
     return this.set[`${key}`]; };
}

export default new Settings();