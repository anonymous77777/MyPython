function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}

$(document).ready(function(){
    $("#login").click(function(){

        var user = $("#username").val();
        if (user == "")
        {
            $("#confirm").text("Please enter your email address.");
            $("#username").focus();
            return false;
        }
        var pwd = $("#password").val();
        if(pwd == "")
        {
            $("#confirm").text("Please enter your password.");
            $("#password").focus();
            return false;
        }

        var pd = {"username":user, "password":pwd, "_xsrf":getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/",
            data:pd,
            cache:false,
            success:function(data){
                if (data == "#")
                    $("#confirm").text("There is no this user.")
                else if (data == "~")
                    $("#confirm").text("your password was not right.")
                else
                    window.location.href = "/index?user="+data;
            },
            error:function(){
                alert("login error!");
            },
        });
    });
});