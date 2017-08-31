function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}

$(document).ready(function(){
    $("#logout").click(function(){
        var pd = {"type":"button", "id":"logout", "_xsrf":getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/index",
            data:pd,
            cache:false,
            success:function(data){
//                $("#logout").text("logout now")
//                alert('ha')
            },
            error:function(){
                alert("logout error!");
            },
        });
    });
    $("#lout").click(function(){
        var pd = {"type":"button", "id":"lout", "_xsrf":getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/index",
            data:pd,
            cache:false,
            success:function(data){
            },
            error:function(){
                alert("lout error!");
            },
        });
    });
});