 
 #include "textures.inc"
 
 camera { location <5, 0, 0> look_at<0, 0, 0> }
 
 light_source {
    <0,-10,0> 
    color rgb<2, 2, 2>
 }   
 
 light_source {
    <20, 15, 0>
    color rgb <1, 1, 1>
    }

 object {
    difference {
        object {
            union {   
                 sphere{
                 <0, 0, 0>, 2
                 color rgb<1, 1, 1>  
                 pigment { rgb <1, 1, 1> }
                 }
                 
                 sphere{
                     <1.3, 0, 0>, 1
                     color rgb<1, 1, 1>  
                     pigment { rgb <0, 1, 0> }
                 } 
            }     
        }  
        object{   
           intersection { 
              cone {
                 <4, 0, 0>, 0
                 <1.87, 0, 0>, 0.5
                   pigment { rgb <0.5, 0, 0> }
                 } 
               sphere {  
                 <1.87,0,0>, 0.5
                 color rgb <0.5, 0, 0>
               } 
            }
        }
    }
 }   
 sphere {   
    <0, 0 , 0>, 2.155
    texture{NBglass}
 }  