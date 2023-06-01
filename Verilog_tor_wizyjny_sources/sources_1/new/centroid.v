`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 26.04.2023 18:35:20
// Design Name: 
// Module Name: centroid
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


module centroid#(
    parameter IMG_H = 64, 
    parameter IMG_W = 64
    )
    (
    input clk,

    input de,
    input hsync,
    input vsync,
    input mask,
    output[11:0] x,
    output[11:0] y
    );
    
    reg[11:0] pos_x = 1;
    reg[11:0] pos_y = 1;
    reg[11:0] x_out;
    reg[11:0] y_out;
    reg eof;
    reg[19:0] m00;
    reg[31:0] mx_prev;
    reg[31:0] my_prev;
    reg p_vsync;
    wire[31:0] x_after_div;
    wire[31:0] y_after_div;
    wire qvx;
    wire qvy;
    reg qv_exist = 1;
    
    
    always @(posedge clk) begin
        p_vsync <= vsync;
        if(de) begin
            pos_x <= pos_x + 1;
        end
    
        if(pos_x == IMG_W) begin
            pos_y <= pos_y +1;
            pos_x <= 1;
        end
        if (pos_y == (IMG_H) & pos_x == (IMG_W - 1) & qv_exist) begin
            eof <= 1;
            qv_exist <= 0;
        end 
        if (eof) begin 
            eof <= 0;
        end
   
       if(qvx & qvy) begin
            x_out = x_after_div[11:0];
            y_out = y_after_div[11:0];
            mx_prev <=0;
            my_prev <= 0;
            m00 <= 0;
            pos_x = 1;
            pos_y = 1;
            qv_exist <= 1;
       end
       
       if(p_vsync == 0 & vsync == 1) begin
            mx_prev <=0;
            my_prev <= 0;
            m00 <= 0;
            pos_x = 1;
            pos_y = 1;
       end
       
        
        
        
        
       if (mask & de & qv_exist ) begin
            m00 = m00 +1;
            mx_prev = mx_prev + pos_x;
            my_prev = my_prev + pos_y;
       end
   end
    

   divider_32_20 div_x(
      .clk(clk),
      .start(eof),
      .dividend(mx_prev),
      .divisor(m00),
      .quotient(x_after_div),
      .qv(qvx)
    );
    
   divider_32_20 div_y(
      .clk(clk),
      .start(eof),
      .dividend(my_prev),
      .divisor(m00),
      .quotient(y_after_div),
      .qv(qvy)
    );    

//    acc akumulator_x(
//        .A(mx_prev),
//        .B({20'd0,pos_x}),
//        .CE(mask & de),
//        .SCLR(eof),
//        .S(mx)
//          );
          
//    acc akumulator_y(
//        .A(my_prev),
//        .B({20'd0,pos_y}),
//        .CE(mask & de),
//        .SCLR(eof),
//        .S(my)
//    );

    assign x = x_out;
    assign y = y_out;
    

    
endmodule
