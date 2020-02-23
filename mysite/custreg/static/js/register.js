var stuD={};
var nowclosed=true;
function webInput() {
    stuD.stuid=$('#stuid').val().replace(/[&<>"'\/]/g,'?');
    stuD.name=$('#name').val().replace(/[&<>"'\/]/g,'?')
    stuD.department=$('#department option:selected').text();
    stuD.sex=$('#sex option:selected').text()
    stuD.conNum=$('#contestStatus').attr('value3');
    if(stuD.name==''||stuD.stuid==''|| stuD.department==null){
        alert('输入存在空白，请检查输入');
        return false;
    }
    return true;
}
function getDate(strDate) { 
    var st = strDate; 
    var a = st.split("_"); 
    var b = a[0].split("-"); 
    var c = a[1].split(":");
    b[1]=Number(b[1])-1;
    var date = new Date(b[0], b[1], b[2], c[0], c[1], c[2]);
    return date; 
  } 
(function(){
    ntime = new Date();
    console.log($('#contestStatus').attr('value2'))
    time = getDate($('#contestStatus').attr('value2'));
    if($('#contestStatus').attr('value1')=='False'){
        console.log('false');
    }
    if($('#contestStatus').attr('value1')=='False'||ntime>time){
        nowclosed=false;
        alert("比赛已截止报名");
    }
    // console.log($('#contestStatus').attr('value'));
})()
$('#submit').on('click',function(){

    if(webInput()&&nowclosed){
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
    }else {
        alert("比赛已截止报名");
    }
});

