`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 16.05.2023 19:09:36
// Design Name: 
// Module Name: cetroid_rectangle
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


module vis_rectangle #    
    (
        parameter IMG_H = 64, 
        parameter IMG_W = 64
    )
    (  
        input clk,
        input de,
        input hsync,
        input vsync,
        input[11:0] x1,
        input[11:0] y1,
        input[11:0] x2,
        input[11:0] y2,
        input[23:0] pixel_in,
        output[23:0] pixel_out,
        output hsync_out,
        output vsync_out,
        output de_out
    );
    reg p_vsync;
    reg [11:0]pos_x = 1; //wertykalnie - kolumny
    reg [11:0]pos_y = 1; //horyzontalnie - rzêdy
    reg eof;
    reg[23:0] new_color;
    
    always @(posedge clk)
    begin
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
       if (((pos_x == x1) | (pos_x == x2) | (pos_y == y1) | (pos_y == y2)) & ((pos_x >= x1) & (pos_x <= x2)) & ((pos_y >= y2) & (pos_y <= y1))) begin
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
