const mongoose = require("mongoose")

if (process.env.NODE_ENV === 'production'){
    var mongoDB = process.env.MONGO_URI_PROD
}

else{
    var mongoDB = process.env.MONGO_URI_DEV
}


mongoose.connect(mongoDB, {useNewUrlParser: true, useUnifiedTopology: true})

const db = mongoose.connection

db.on('error',console.error.bind(console, 'Fallo conexion BD!!'))
db.once('open', () =>{
    console.log("Conectado")
})