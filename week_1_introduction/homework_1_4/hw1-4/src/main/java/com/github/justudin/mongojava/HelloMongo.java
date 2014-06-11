package com.github.justudin.mongojava;

import com.mongodb.*;

import java.net.UnknownHostException;

/**
 * Created by udin on 6/5/2014.
 */
public class HelloMongo {
    public static void main(String[] args)  throws UnknownHostException{
        MongoClient client = new MongoClient(new ServerAddress("localhost", 27017));

        DB database = client.getDB("test");
        DBCollection collection = database.getCollection("users");

        DBObject document = collection.findOne();
        System.out.println(document);
    }
}
