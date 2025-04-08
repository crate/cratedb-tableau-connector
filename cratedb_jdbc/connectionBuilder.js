(function dsbuilder(attr) {
    var urlBuilder = "jdbc:postgresql://" + attr[connectionHelper.attributeServer] + ":" + attr[connectionHelper.attributePort] + "/" + attr[connectionHelper.attributeDatabase] + "?useCursorFetch=true&defaultRowFetchSize=100&autoCommit=false";

    return [urlBuilder];
})
