// location = {
//     "ancestorOrigins": {},
//     "href": "http://mpa.hubei.gov.cn/zfxxgk/fdzdgknr/cpzh/index.shtml",
//     "origin": "http://mpa.hubei.gov.cn",
//     "protocol": "http:",
//     "host": "mpa.hubei.gov.cn",
//     "hostname": "mpa.hubei.gov.cn",
//     "port": "",
//     "pathname": "/zfxxgk/fdzdgknr/cpzh/index.shtml",
//     "search": "",
//     "hash": ""
//     };

// // function Document(){

// //     this.ele_scr = {
// //         "getAttribute": function(attr){
// //             if (attr = "r"){return "m"}
// //         },
// //         "parentElement": {
// //             "removeChild":function(tag){
// //                 return tag
// //             }
// //         }
// //     },

// //     this.scripts = [this.ele_scr, this.ele_scr],


// //     this.getElementsByTagName = function(tagname){
// //         if (tagname == "script"){
// //             return this.scripts
// //         }
// //     }
// // };


// // function localStorage(){
// //     this.dict = {},
// //     this.setItem = function(key, value){
// //         this.dict[key] = value
// //     },
// //     this.getItem = function(key){
// //         try {
// //             return this.dict[key]
// //         } catch(e){
// //             return null
// //         }
// //     },
// //     this.removeItem = function(key){
// //         delete this.dict[key]
// //     }
// // };

// // function sessionStorage(){
// //     this.dict = {},
// //     this.setItem = function(key, value){
// //         this.dict[key] = value
// //     },
// //     this.getItem = function(key){
// //         try {
// //             return this.dict[key]
// //         } catch(e){
// //             return null
// //         }
// //     },
// //     this.removeItem = function(key){
// //         delete this.dict[key]
// //     }
// // };

// // document = new Document();
// // ls = new localStorage();

// // window = {
// //     $_ts: {},
// //     eval: function (data) {
// //         eval_js = data
// //     },
// //     "top":location,
// //     "location":location,
// //     "document": document,
// //     "localStorage":{},
// //     "sessionStorage":{},
// //     "setInterval":function(){
// //         return setInterval
// //     },
// //     "addEventListener":function(data){
// //     }
// // };


// // var re = new RegExp("ab+c");


// localStorage = {
//     removeItem: function (key) {
//         delete this[key]
//     },
//     getItem: function (key) {
//         return this[key] ? this[key]: null;
//     },
//     setItem: function (key, value) {
//         this[key] = "" + value;  
//     },
// };



// // window = {
// //     $_ts: {},
// //     eval: function (data) {
// //         eval_js = data
// //     },
// //     "top":location,
// //     "location":location,
// //     "document": {},
// //     "localStorage":localStorage,
// //     "sessionStorage":{},
// //     "setInterval":function(){
// //         return setInterval
// //     },
// //     "addEventListener":function(data){
// //     },
// //     "self":f_self()
// // };



// // console.log(window["self"])
// // localStorage.setItem("a", "b")
// // console.log(window["localStorage"])
// // console.log(window["localStorage"]["getItem"]("a"))



// function Fwindow(){
//     this.$_ts={},
//     this.self = this,
//     this.location = location
//     this.eval = function(data){
//         eval_js = data
//     },
//     this.localStorage = localStorage
// }

// window = new Fwindow()

// window.$_ts["a"] = "b"
// console.log(window["self"])


// window = {
//     $_ts: {},
//     eval: function (data) {
//         eval_js = data
//     },
//     "top":location,
//     "location":location,
//     "localStorage":localStorage,
//     "sessionStorage":sessionStorage,
//     "document":document,
//     "setInterval":function(){
//         return setInterval
//     },
//     "setTimeout": setTimeout,
//     "addEventListener": function(){
//         return {"script": "add"}
//     },
//     "RegExp":RegExp,
//     "escape":escape,
//     "decodeURIComponent":decodeURIComponent,
//     "isFinite":isFinite,
//     "clearInterval":clearInterval,
//     "Math": Math,
//     "DOMParser": DOMParser,
//     "JSON": JSON,
//     "parseFloat":parseFloat,
//     "parseInt":parseInt,
//     "self":globalThis
// };

// function Fwindow(){
//     this.$_ts={},
//     this.eval = function(data){
//         eval_js = data
//     },
//     this.location = location,
//     this.top = location,
//     this.localStorage = localStorage,
//     this.sessionStorage = this.sessionStorage,
//     this.document = document,
//     this.setInterval = setInterval,
//     this.setTimeout = setTimeout,
//     this.addEventListener = function(){
//         return {"script":"add"}
//     },
//     this.RegExp = RegExp,
//     this.escape = escape,
//     this.decodeURIComponent = decodeURIComponent,
//     this.isFinite = isFinite,
//     this.clearInterval = clearInterval,
//     this.Math = Math,
//     this.DOMParser = DOMParser,
//     this.JSON = JSON,
//     this.parseFloat = parseFloat,
//     this.parseInt = parseInt,
//     this.self = this
// }

// window = new Fwindow()


function Document(content){

    this.cookie = '',

    this.content = content

    this.ele_scr = {
        "getAttribute": function(attr){
            if (attr = "r"){return "m"}
        },
        "parentElement": {
            "removeChild":function(tag){
                return tag
            }
        }
    },

    this.metas = [
        {
            "getAttribute": function(attr){
                if (attr = "r"){return "m"}
                else if (attr = "content"){return "text/html; charset=utf-8"}
            },
            "parentNode": {
                "removeChild":function(tag){
                    return tag
                }
            }
        },
        {
            "content": this.content,
            "getAttribute": function(attr){
                if (attr = "r"){return "m"}
                else if (attr = "content"){return this.content}
            },
            "parentNode": {
                "removeChild":function(tag){
                    return tag
                }
            }
        }
    ],

    this.ele_div = {
        "getElementsByTagName" : function(tag){
            if (tag == "i"){
                return []
            }
        }
    },

    this.scripts = [this.ele_scr, this.ele_scr],


    this.getElementsByTagName = function(tagname){
        if (tagname == "script"){
            return this.scripts
        } else if (tagname == "meta"){
            return this.metas
        } else if (tagname == "base"){return []}
    },

    this.getElementById = function(tagname){
        if (tagname == "root-hammerhead-shadow-ui"){
            return null
        } else{
            console.log("tagname")
        }
    },

    this.documentElement = {
        "style":{}
    },

    this.createElement = function(tag){
        if (tag == "div"){
            return this.ele_div
        }
    }
};

document = new Document(".bhe5h3z0y2VT3HJfGWR8_rbpgg4_3dm0qhAPnecRXTeZCw6zSdeli4v1vusapryIHWe3jj5nq9");

m = document.getElementsByTagName("meta")
console.log(m[1]["content"])