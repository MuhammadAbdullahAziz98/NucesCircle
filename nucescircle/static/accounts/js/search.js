function searchBar(datasource,source,text1,text2,text3,prop1,prop2,prop3) {
    var searchBar = document.querySelector('#searchbar');
        var x = document.createElement('div');
        var peopleSearchBar='<form class="pt-3">'+
                
                '                            <div class="form-row">'+
                                               ' <div class="mx-sm-3 mx-2 my-auto searchform"><strong>Search:</strong></div>'+
                                                '<div class="col">'+
                                                   ' <input type="text" class="form-control searchform" placeholder="'+text1+'" id="search'+text1+'">'+
                                                '</div>'+
                                                '<div class="col">'+
                                                   ' <input type="text" class="form-control searchform" placeholder="'+text2+'" id="search'+text2+'">'+
                                                '</div>'+
                                                '<div class="col">'+
                                                       ' <input type="text" class="form-control searchform" placeholder="'+text3+'" id="search'+text3+'">'+
                                                '</div>'+
                                                '<div class="col">'+
                                                   ' <button class="mx-1 mx-sm-0 btn btn-primary searchform" '+ 'type="button" id="searcher">Search</button>'+
                                               ' </div></div></form>';
        x.innerHTML = peopleSearchBar;
        searchBar.appendChild(x);
        inpS = document.getElementById("searcher");
        s1 = "search"+text1;
        s2 = "search"+text2;
        s3 = "search"+text3;
        inpS.addEventListener("click", function(){
            searchFun(datasource,s1,s2,s3,prop1,prop2,prop3)
        });
        return false;
 }
 names= "";
 cal1= true;
 cal2 = true;
 cal3 = true;
 function searchFun(people,text1,text2,text3,prop1,prop2,prop3){
    cal1= true;
    cal2 = true;
    cal3 = true;
    console.log(people);
    if (!document.getElementById(text1).value.replace(/\s/g, '').length) {
        console.log(prop1.toString().toUpperCase() + ' only contains whitespace (ie. spaces, tabs or line breaks)');
        cal1 = false;
    }
    if (!document.getElementById(text2).value.replace(/\s/g, '').length) {
        console.log(prop2.toString().toUpperCase() + ' only contains whitespace (ie. spaces, tabs or line breaks)');
        cal2 = false;
    }
    if (!document.getElementById(text3).value.replace(/\s/g, '').length) {
        console.log(prop3.toString().toUpperCase() + ' only contains whitespace (ie. spaces, tabs or line breaks)');
        cal3 = false;
    }
    val1 = document.getElementById(text1).value.toLowerCase();
    val2 = document.getElementById(text2).value.toLowerCase();
    val3 = document.getElementById(text3).value.toLowerCase();
    res="";
    name="",email="",degree="";
    var results = document.querySelector('#results');
    while (results.firstChild) {
        results.removeChild(results.firstChild);
    }
    for(i =0;i<people.length;i++){
        propVal1 = people[i][prop1].toString().toLowerCase();
        alert(propVal1);
        propVal2 = people[i][prop2].toString().toLowerCase();
        propVal3 = people[i][prop3].toString().toLowerCase();
        
        if(cal1){
            if(cal2){
                if(cal3){
                    if(propVal1.indexOf(val1) != -1 && propVal2.indexOf(val2) != -1 && propVal3.indexOf(val3)!=-1){
                        res = people[i][prop1];
                            console.log(res);
                        name = people[i][prop1];
                        email = people[i][prop2];
                        degree= people[i][prop3];
                        var d = document.createElement('div');
                        card='                    <div class="poster-background poster-border mt-3">'+
                        '<div class="card">'+
                        '       <div class="card-body">'+
                                    
                                '    <h4 class="card-title">'+name+'</h4>'+
                                '    <h6 class="text-muted card-subtitle">'+email+'</h6>'+
                                    '<p class="card-text">'+degree+'</p>'+
                                   ' <a class="btn btn-outline-primary" href="#">Connect</a>'+
                                '</div></div>'

                                d.innerHTML = card;
                                results.appendChild(d);

                    }
                }
                else{
                    if(propVal1.indexOf(val1) != -1 && propVal2.indexOf(val2) != -1){
                        res = people[i][prop1];
                            console.log(res);
                            name = people[i][prop1];
                            email = people[i][prop2];
                            degree= people[i][prop3];
                            var d = document.createElement('div');
                            card='                    <div class="poster-background poster-border mt-3">'+
                            '<div class="card">'+
                            '       <div class="card-body">'+
                                        
                                    '    <h4 class="card-title">'+name+'</h4>'+
                                    '    <h6 class="text-muted card-subtitle">'+email+'</h6>'+
                                        '<p class="card-text">'+degree+'</p>'+
                                       ' <a class="btn btn-outline-primary" href="#">Connect</a>'+
                                    '</div></div>'
    
                                    d.innerHTML = card;
                                    results.appendChild(d);
                          
                    }
                }
            }
            else{
                if(cal3){
                    if(propVal1.indexOf(val1) != -1 && propVal3.indexOf(val3)!=-1){
                        res = people[i][prop1];
                            console.log(res);
                            name = people[i][prop1];
                            email = people[i][prop2];
                            degree= people[i][prop3];
                            var d = document.createElement('div');
                            card='                    <div class="poster-background poster-border mt-3">'+
                            '<div class="card">'+
                            '       <div class="card-body">'+
                                        
                                    '    <h4 class="card-title">'+name+'</h4>'+
                                    '    <h6 class="text-muted card-subtitle">'+email+'</h6>'+
                                        '<p class="card-text">'+degree+'</p>'+
                                       ' <a class="btn btn-outline-primary" href="#">Connect</a>'+
                                    '</div></div>'
    
                                    d.innerHTML = card;
                                    results.appendChild(d);
                            
                    }
                }
                else{
                    if(propVal1.indexOf(val1) != -1){
                        res = people[i][prop1];
                            console.log(res);
                            name = people[i][prop1];
                            email = people[i][prop2];
                            degree= people[i][prop3];
                            var d = document.createElement('div');
                            card='                    <div class="poster-background poster-border mt-3">'+
                            '<div class="card">'+
                            '       <div class="card-body">'+
                                        
                                    '    <h4 class="card-title">'+name+'</h4>'+
                                    '    <h6 class="text-muted card-subtitle">'+email+'</h6>'+
                                        '<p class="card-text">'+degree+'</p>'+
                                       ' <a class="btn btn-outline-primary" href="#">Connect</a>'+
                                    '</div></div>'
    
                                    d.innerHTML = card;
                                    results.appendChild(d);
                            
                    }
                }
            }
        } 
        else{
            if(cal2){
                if(cal3){
                    if(propVal2.indexOf(val2) != -1 && propVal3.indexOf(val3)!=-1){
                        res = people[i][prop1];
                            console.log(res);
                            name = people[i][prop1];
                            email = people[i][prop2];
                            degree= people[i][prop3];
                            var d = document.createElement('div');
                            card='                    <div class="poster-background poster-border mt-3">'+
                            '<div class="card">'+
                            '       <div class="card-body">'+
                                        
                                    '    <h4 class="card-title">'+name+'</h4>'+
                                    '    <h6 class="text-muted card-subtitle">'+email+'</h6>'+
                                        '<p class="card-text">'+degree+'</p>'+
                                       ' <a class="btn btn-outline-primary" href="#">Connect</a>'+
                                    '</div></div>'
    
                                    d.innerHTML = card;
                                    results.appendChild(d);
                          
                    }

                }
                else{
                    if(propVal2.indexOf(val2) != -1){
                        res = people[i][prop1];
                            console.log(res);
                            name = people[i][prop1];
                            email = people[i][prop2];
                            degree= people[i][prop3];
                            var d = document.createElement('div');
                            card='                    <div class="poster-background poster-border mt-3">'+
                            '<div class="card">'+
                            '       <div class="card-body">'+
                                        
                                    '    <h4 class="card-title">'+name+'</h4>'+
                                    '    <h6 class="text-muted card-subtitle">'+email+'</h6>'+
                                        '<p class="card-text">'+degree+'</p>'+
                                       ' <a class="btn btn-outline-primary" href="#">Connect</a>'+
                                    '</div></div>'
    
                                    d.innerHTML = card;
                                    results.appendChild(d);
                     
                    }

                }
            }
            else{
                if(cal3){
                    if(propVal2.indexOf(val2) != -1 && propVal3.indexOf(val3)!=-1){
                        res = people[i][prop1];
                            console.log(res);
                            name = people[i][prop1];
                            email = people[i][prop2];
                            degree= people[i][prop3];
                            var d = document.createElement('div');
                            card='                    <div class="poster-background poster-border mt-3">'+
                            '<div class="card">'+
                            '       <div class="card-body">'+
                                        
                                    '    <h4 class="card-title">'+name+'</h4>'+
                                    '    <h6 class="text-muted card-subtitle">'+email+'</h6>'+
                                        '<p class="card-text">'+degree+'</p>'+
                                       ' <a class="btn btn-outline-primary" href="#">Connect</a>'+
                                    '</div></div>'
    
                                    d.innerHTML = card;
                                    results.appendChild(d);
                          
                    }

                }
                else{
                    if(cal3){
                        if(propVal2.indexOf(val2) != -1){
                            res = people[i][prop1];
                            console.log(res);
                            name = people[i][prop1];
                            email = people[i][prop2];
                            degree= people[i][prop3];
                            var d = document.createElement('div');
                            card='                    <div class="poster-background poster-border mt-3">'+
                            '<div class="card">'+
                            '       <div class="card-body">'+
                                        
                                    '    <h4 class="card-title">'+name+'</h4>'+
                                    '    <h6 class="text-muted card-subtitle">'+email+'</h6>'+
                                        '<p class="card-text">'+degree+'</p>'+
                                       ' <a class="btn btn-outline-primary" href="#">Connect</a>'+
                                    '</div></div>'
    
                                    d.innerHTML = card;
                                    results.appendChild(d);
                            }
                    }

                }

            }
        }
        
    }
   
};
