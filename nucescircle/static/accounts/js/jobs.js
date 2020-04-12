id = 0;
function addSkill(){
    var elm = document.querySelector('#skills');
    var z = document.createElement('input'); // is a node
    z.classList.add("mb-5");
    z.classList.add("form-control");
    id++
    z.id = 'skill' + id;
    z.name = "skill"
    z.required = true;
    elm.append(z);
    return false;
}
