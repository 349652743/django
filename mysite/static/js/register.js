var stuD={};
function webInput() {
    stuD.stuid=$('#stuid').val().replace(/[&<>"'\/]/g,'?');
    stuD.name=$('#name').val().replace(/[&<>"'\/]/g,'?')
    stuD.department=$('#department option:selected').text();
    stuD.sex=$('#sex option:selected').text()

    if(stuD.name==''||stuD.stuid==''|| stuD.department==null){
        alert('输入存在空白，请检查输入');
        return false;
    }
    return true;
}
$('#submit').on('click',function(){
    if(webInput()){
        $.ajax({
            url:"/custreg/reg_user/",
            type:"POST",
            data:stuD,
            success:function(data){
                if(data['message']){
                    alert(data['message'])
                }
            }
            
        });
    }
});
