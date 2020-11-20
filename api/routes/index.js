const express = require("express");
const router = express.Router();
require('dotenv').config()
// const mongoose = require('mongoose')
const {MongoClient} = require('mongodb');
const uri = process.env.MONGO
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true })

 
async function mongoLast() {try {
    // Connect to the MongoDB cluster
    await client.connect();

    // Make the appropriate DB calls
    var options = {
        "limit": 1,
        "sort": ["_id", 'desc']
    }

    const database = client.db("badnews")
    const collection = database.collection("articles")

    article = await collection.find({}, options)

    console.log(article)
} catch (e) {
    console.error(e);
} finally {
    await client.close();
}

}

/* GET home page. */
router.get("/", function(req, res, next) {
//   res.render("index", { title: "Express" });
    mongoLast()
});

module.exports = router;


