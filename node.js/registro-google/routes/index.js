const passport = require('passport');
let  GoogleStrategy = require( 'passport-google-oauth2' ).Strategy;

passport.use(new GoogleStrategy({
    clientID:     process.env.GOOGLE_CLIENT_ID,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    callbackURL: "http://localhost:3000/google/callback",
    passReqToCallback   : true
  },
  function(request, accessToken, refreshToken, profile, done) {

    return done(null,profile)
  },



));
var express = require('express');
var router = express.Router();
require("../routes/auth")


const isloged = (req,res,next)=>{
  req.user ? next() : res.sendStatus(401)

}

/* GET home page. */
router.get('/', (req, res, next)=> {
 
  res.send("<a href='/auth/google'>Autenticate con GOOGLE</a>")
  // res.render('index', { title: 'Express' });
});


router.get("/auth/google",
  passport.authenticate("google",{scope:["email","profile"]

  })

)


router.get("/google/callback",
  passport.authenticate("google",{
    successRedirect:"/protected",
    failureRedirect:"/auth/failure"

  })

)

router.get('/auth/failure', (req, res, next)=> {
 
  res.send("ESTE ES EL FALLO")
});


router.get('/protected', isloged, (req, res, next)=> {
 
  res.send(`Hola ${req.user.displayName }`)
});

router.get('/logout', function (req, res, next){
  req.logOut()
  res.send("Adios amigo")
});

module.exports = router;