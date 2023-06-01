`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 16.05.2023 19:10:29
// Design Name: 
// Module Name: centroid_kolo
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module centroid_kolo#
    (
    parameter IMG_H = 64, 
    parameter IMG_W = 64,
    parameter RADIUS = 5,
    parameter RADIUS_POWER2 = 25
    )
    (  
    input clk,
    input de,
    input hsync,
    input vsync,
    input[11:0] x,
    input[11:0] y, 
    input[23:0] pixel_in,
    
    output[23:0] pixel_out,
    output hsync_out,
    output vsync_out,
    output de_out
    
    
    );
    reg[11:0]maxX = IMG_W - RADIUS;
    reg[11:0]maxY = IMG_H - RADIUS;
    reg[11:0] pos_x = 1;
    reg[11:0] pos_y = 1;
    wire signed[12:0] diff_x ;
    wire signed[12:0] diff_y ;
    reg[23:0] new_color;
    wire signed[26:0]power_x;
    wire signed[26:0]power_y;
    wire[23:0]power_R;
    reg eof;
    reg p_vsync;
    
    always @(posedge clk) begin
        p_vsync <= vsync;
        if(de) begin
            pos_x <= pos_x + 1;
        end
        if(pos_x >= IMG_W) begin
            pos_y <= pos_y +1;
            pos_x <= 1;
        end
        if ((pos_y >= IMG_H) & (pos_x >= IMG_W-1)) begin
            eof <= 1;
        end else begin
            eof <= 0;
        end 
        if (eof) begin
            pos_x = 1;
            pos_y = 1;
        end
        if(p_vsync == 0 & vsync == 1) begin
            pos_x = 1;
            pos_y = 1;
       end
    if( ((RADIUS < pos_x) & (pos_x < maxX) & (power_R < RADIUS_POWER2)) |(pos_x == x | pos_y == y)) begin
        new_color = {8'hff,8'h00,8'h00};
    end else begin
        new_color = pixel_in;
    end

            
    end
    
    Odejmowacz diff_I_X
    (
    .A(pos_x),
    .B(x),
    .S(diff_x)
    );
    Odejmowacz diff_J_Y
    (
    .A(pos_y),
    .B(y),
    .S(diff_y)
    );
    
    kwadrat x_potega(
        .A(diff_x),
        .B(diff_x),
        .P(power_x)
    );
    
    kwadrat y_potega(
        .A(diff_y),
        .B(diff_y),
        .P(power_y)
    );
    
    kwadrat_promien nazwa(
        .A(power_x),
        .B(power_y),
        .S(power_R)
    );

   assign pixel_out = new_color;
   assign vsync_out = vsync;
   assign hsync_out = hsync;
   assign de_out = de;
    
endmodule
