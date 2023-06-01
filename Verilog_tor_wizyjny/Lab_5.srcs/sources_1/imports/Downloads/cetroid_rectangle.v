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


module cetroid_rectangle #
    ( parameter IMG_H=64, 
    parameter IMG_W=64 )
    (
    input clk,
    input de,
    input hsync,
    input vsync,
    input mask,
    
    output[11:0] xP_line ,
    output[11:0] xL_line ,
    output[11:0] yG_line ,
    output[11:0] yD_line ,
    output[11:0] y_licznik ,
    output[11:0] x_licznik ,
    output in_mask,
    
    output [11:0]x1,
    output [11:0]x2,
    output [11:0]y1,
    output [11:0]y2

    
    );
    
    reg [11:0] x_L = IMG_W;
    reg [11:0] x_P = 0;
    reg [11:0] y_G = 0;
    reg [11:0] y_D = IMG_H;
    
    reg [11:0]pos_x = 1; //wertykalnie - kolumny
    reg [11:0]pos_y = 1; //horyzontalnie - rzêdy

    reg p_vsync;
    reg [11:0]x1_out;
    reg [11:0]x2_out;
    reg [11:0]y1_out;
    reg [11:0]y2_out;
    reg eof;
    
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
            x1_out = x_L;
            x2_out = x_P; 
            y1_out = y_G;
            y2_out = y_D; 
        end else begin
            eof <= 0;
        end 
        if (eof) begin
            pos_x = 1;
            pos_y = 1;
            x_L = IMG_W ;
            x_P = 0;
            y_G = 0;
            y_D = IMG_H;

                       
        end
        if(p_vsync == 0 & vsync == 1) begin
            pos_x = 1;
            pos_y = 1;
            x_L = IMG_W;
            x_P = 0;
            y_G = 0;
            y_D = IMG_H; 
       end
     if (mask & de) begin
        if (x_L > pos_x) begin 
            x_L <= pos_x;
        end
        if (x_P < pos_x & pos_x < 12'd1270) begin
            x_P <= pos_x; 
        end
        if (y_D > pos_y) begin y_D <= pos_y; end
        if (y_G < pos_y) begin y_G <= pos_y; end
    end       
end
   
assign x1 = x1_out;
assign x2 = x2_out;
assign y1 = y1_out;
assign y2 = y2_out;
assign xP_line = x_P;
assign xL_line = x_L;
assign yG_line = y_G;
assign yD_line = y_D;
assign y_licznik = pos_y;
assign x_licznik = pos_x;
assign in_mask = mask;
       
endmodule
