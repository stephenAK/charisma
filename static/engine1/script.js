// -----------------------------------------------------------------------------------
// http://wowslider.com/
// JavaScript Wow Slider is a free software that helps you easily generate delicious 
// slideshows with gorgeous transition effects, in a few clicks without writing a single line of code.
// Generated by WOW Slider 4.7
//
//***********************************************
// Obfuscated by Javascript Obfuscator
// http://javascript-source.com
//***********************************************
function ws_book(i,g,a){var d=jQuery;var e=d("ul",a);var c=i.duration;var b={backgroundColor:"#000",position:"absolute",left:0,top:0,"float":"left",width:"100%",height:"100%",transformStyle:"preserve-3d",zIndex:3,outline:"1px solid transparent"};var f;this.go=function(p,n){if(h.cssTransitions()&&h.cssTransforms3d()&&!document.all){if(f){return n}var s=g.get(p),k=g.get(n);var l=((n==0&&p!=n+1)||(p==n-1))?{p:true,cont1back:s.src,cont2back:k.src,item1back:k.src,item2back:s.src,item1deg:"0.1deg",item2deg:"-90deg",item1dodeg:"90deg",item2dodeg:"0deg",trans1:"ease-in ",trans2:"ease-out "}:{p:false,cont1back:k.src,cont2back:s.src,item1back:s.src,item2back:k.src,item1deg:"90deg",item2deg:"-0.1deg",item1dodeg:"0deg",item2dodeg:"-90deg",trans1:"ease-out ",trans2:"ease-in "};var t=d("<div>").css(b).css({background:"url("+l.cont1back+")",backgroundSize:"auto 100%",width:"50%"}).appendTo(a.parent());var q=d("<div>").css(b).css({left:"50%",background:"url("+l.cont2back+") right",backgroundSize:"auto 100%",width:"50%"}).appendTo(a.parent());var o=d("<div>").css(b).css({background:"url("+l.item1back+")",backgroundSize:"auto 100%",marginRight:"-100%",transform:"rotateY("+l.item1deg+")",transition:l.trans1+c/2000+"s","transform-origin":"right","z-index":8}).appendTo(t);var m=d("<div>").css(b).css({background:"url("+l.item2back+") right",backgroundSize:"auto 100%",marginRight:"-100%",transform:"rotateY("+l.item2deg+")",transition:l.trans2+c/2000+"s","transform-origin":"left"}).appendTo(q);var r=d("<div>").css(b).css({opacity:0.2,zIndex:2}).appendTo((l.p?t:q)).css("opacity",1).clone().appendTo((l.p?m:o)).css("opacity",0.2).clone().appendTo((l.p?q:t)).css("opacity",1).hide().clone().appendTo((l.p?o:m)).css("opacity",0.2).hide();f=new j(l,t,q,o,m,function(){e.css({left:-p+"00%"}).show();t.remove();q.remove();f=0})}else{a.find("ul").stop(true).animate({left:(p?-p+"00%":(/Safari/.test(navigator.userAgent)?"0%":0))},i.duration,"easeInOutExpo")}function j(A,E,D,C,B,F){var z=E,y=D,x=C,w=B,v="rotateY("+A.item1dodeg+")";var u="rotateY("+A.item2dodeg+")";if(!A.p){z=D;y=E;x=B;w=C;v="rotateY("+A.item2dodeg+")";u="rotateY("+A.item1dodeg+")"}a.parent().css("perspective",w.width()*4);x.css("transform",v);x.children().fadeIn(c/2);z.children().fadeOut(c/2,function(){w.css("transform",u);w.children().fadeOut(c/2);y.children().fadeIn(c/2)});setTimeout(F,c);return{stop:function(){F()}}}return p};var h={domPrefixes:" Webkit Moz ms O Khtml".split(" "),testDom:function(k){var j=this.domPrefixes.length;while(j--){if(typeof document.body.style[this.domPrefixes[j]+k]!=="undefined"){return true}}return false},cssTransitions:function(){return this.testDom("Transition")},cssTransforms3d:function(){if(typeof document.body.style.perspectiveProperty!=="undefined"){return true}return this.testDom("Perspective")}}};// -----------------------------------------------------------------------------------
// http://wowslider.com/
// JavaScript Wow Slider is a free software that helps you easily generate delicious 
// slideshows with gorgeous transition effects, in a few clicks without writing a single line of code.
// Generated by WOW Slider 4.7
//
//***********************************************
// Obfuscated by Javascript Obfuscator
// http://javascript-source.com
//***********************************************
jQuery("#wowslider-container1").wowSlider({effect:"book",prev:"",next:"",duration:20*100,delay:30*100,width:320,height:240,autoPlay:true,playPause:true,stopOnHover:false,loop:false,bullets:true,caption:true,captionEffect:"move",controls:true,onBeforeStep:0,images:0});