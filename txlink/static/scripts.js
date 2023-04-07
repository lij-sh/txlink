// 菜单栏收缩展开
function menu_active(ulId){
	if(ulId.style.display == "none"){
		ulId.style.display = "block"
	}else{
		ulId.style.display = "none"
	} }
// 表单编辑和锁定
function edit(){
  if (document.getElementById("editBtn").disabled == false){
    var els = document.getElementsByClassName("cust_info");
    for (let i = 0; i < els.length; i++) {
      els[i].readOnly = false}
    document.getElementById("editBtn").disabled = true
    document.getElementById("saveBtn").disabled = false
    } else{
      document.getElementById("editBtn").disabled = false
    }
}