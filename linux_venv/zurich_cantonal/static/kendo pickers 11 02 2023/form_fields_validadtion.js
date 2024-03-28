/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

function isNumerickey(evt)
{
    var charCode=(evt.which)?evt.which:event.keyCode;
    if(charCode!=46 && charCode>31 && (charCode<48 || charCode>57)){
        //alert('Please enter code');
        return false;
    }
    return true;
 }
        
function isNumerickey1(id)
{
    var value=$("#"+id).val();   
    //alert(value);
    var vali=$.isNumeric(value);
    if(vali==false){        
        //alert
        $("#"+id).val('');  
        
//        $("#form-validate").fadeIn();
//        $("#errortext").text("Please enter only digits");
        $("#"+id).css("border-color","red");
        //document.getElementById(id).focus();
        return false;
    }
    return true;
    //return true;
//    if(vali==true){
//        return true;
//    }else{
//        //$("#"+id).val('');
//        return false;        
//    }
//    var regex=new RegExp(/^\+?[0-9(),.-]+$/);
//    if(value.match(regex)){
//        return true;
//    }else{
//        //$("#"+id).val('');
//        return false;
//    }
 }
            function getValidHH(value,id)
            {
                if(value>23){
                    $("#"+id).val('');
                    $("#errortext").text("Please enter time properly");
                    return false;
                }
            }   
            /*  value, id, text, condition value, numberformat(true/false), active/inactive */
function getValidMM(value,id)
            {
                if(value>59){
                    $("#"+id).val('');
                    $("#errortext").text("Please enter time properly");
                    return false;
                }
            } 
            
function timevalidation()
{
    
}