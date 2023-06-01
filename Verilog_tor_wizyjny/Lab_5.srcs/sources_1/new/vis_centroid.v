`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.05.2023 14:06:40
// Design Name: 
// Module Name: vis_centroid
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


module vis_centroid#
    (
    parameter IMG_H = 64, 
    parameter IMG_W = 64
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
    reg[11:0] pos_x = 1;
    reg[11:0] pos_y = 1;
    reg[23:0] new_color;
    reg p_vsync;
    reg eof = 0;
    
    always @(posedge clk) begin
        p_vsync <= vsync ;
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
        
              
       if ((pos_x == x) | (pos_y == y)) begin
            new_color = {8'hff,8'h00,8'h00};
       end else begin
            new_color = pixel_in;
       end
   end
   
   assign pixel_out = new_color;
   assign vsync_out = vsync;
   assign hsync_out = hsync;
   assign de_out = de;

endmodule
