({
    myAction : function(component, event, helper) {

    },
addToTable : function(component, event, helper) {
    var data = component.get("v.data");
    var dni = event.getParam("ownerDni");
    var name = event.getParam("ownerName");
    var objeto = {ownerDni: dni, ownerName: name}
    data.push(objeto);
//    data.push({
//        ownerDni:event.getParam("ownerDni"),
//        ownerName:event.getParam("ownerName")
//    })
    component.set("v.data",data);
    },
})
