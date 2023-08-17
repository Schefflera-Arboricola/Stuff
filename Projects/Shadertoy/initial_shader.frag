// https://www.shadertoy.com/view/mssBW7

vec3 palette( float t ) {
    vec3 a = vec3(0.75, 0.5, 0.5);
    vec3 b = vec3(0.25, 0.25, 0.25);
    vec3 c = vec3(1.0, 1.0, 1.0);
    vec3 d = vec3(0.45,0.5,0.5);

    return c*tan(a+b*d/t) / b*cos( (6.28318)*(c*t+d)) + c;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord ) {
    vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
    vec2 uv0 = uv;
    vec3 finalColor = vec3(0.2);
    
    for (float i = 0.0; i < 3.; i++) {
        uv = fract(uv*2.718) - 0.5;

        float d = length(uv*2.0) * exp(-length(uv0));

        vec3 col = palette(length(uv0) + i*2.3 + iTime*0.8);

        d = tan(d*10. + iTime)/10.;
        d = fract(d);

        d = pow(0.01 / d, 1.2);

        finalColor += col * d;
    }
        
    fragColor = vec4(finalColor, 1.0);
}