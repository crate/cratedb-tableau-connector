(function propertiesbuilder(attr) {
    var props = {};

    props["user"] = attr[connectionHelper.attributeUsername];

    var authAttrValue = attr[connectionHelper.attributeAuthentication];

    if(authAttrValue == "auth-user-pass"){
       props["password"] = attr[connectionHelper.attributePassword];
    }

    if (attr[connectionHelper.attributeSSLMode] == "require") {
        props["ssl"] = "true";
        props["sslmode"] = "require";
    }

    return props;
})
