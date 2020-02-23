var aduser={};
function webInput() {
    console.log(aduser.username);
    aduser.username=$('#username').val().replace(/[&<>"'\/]/g,'?');
    aduser.password=$('#password').val();
    if(aduser.username==''||aduser.password==''){
        alert('输入存在空白，请检查输入');
        return false;
    }
    return true;
}
$('#submit').on('click',function(){
    if(webInput()){
        $.ajax({
            url:"/question/log/",
            type:"POST",
            data:aduser,
            success:function(data){
                console.log(data['message']);
                if(data['message']){
                    alert(data['message']);
                    if(data['message']==('登陆成功')){
                        window.location.replace("/question/detail/");
                    }else {
                        alert(data['message']);
                    }
                }
            }
        });
    }
});
