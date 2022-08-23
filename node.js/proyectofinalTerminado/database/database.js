const mongoose = require("mongoose")
const db =async () => {

    try{
        await mongoose.connect(process.env.DATABASE,{
 
            useNewUrlParser: true,
            useUnifiedTopology: true,
        }) 

        console.log("Base de datos conectada")


    }catch(err){
        console.log(err)
    }
}
module.exports = db