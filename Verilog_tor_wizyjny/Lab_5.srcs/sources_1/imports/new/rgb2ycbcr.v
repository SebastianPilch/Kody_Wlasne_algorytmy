`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 16.04.2023 18:48:02
// Design Name: 
// Module Name: rgb2ycbcr
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


module rgb2ycbcr(
    input clk,
    input de_in,
    input v_sync_in,
    input h_sync_in,
    input[23:0] pixel_in,
    output de_out,
    output v_sync_out,
    output h_sync_out,
    output[23:0] pixel_out
    );
    
    reg[17:0] matrix_00 = 18'b001001100100010111 ;
    reg[17:0] matrix_01 = 18'b010010110010001011 ;
    reg[17:0] matrix_02 = 18'b000011101001011110 ;
    reg[17:0] matrix_10 = 18'b111010100110011011 ;
    reg[17:0] matrix_11 = 18'b110101011001100101 ;
    reg[17:0] matrix_12 = 18'b010000000000000000 ;
    reg[17:0] matrix_20 = 18'b010000000000000000 ;
    reg[17:0] matrix_21 = 18'b110010100110100010 ;
    reg[17:0] matrix_22 = 18'b111101011001011110 ;
    reg[7:0] R;
    reg[7:0] G;
    reg[7:0] B;
    initial begin
    R = pixel_in[7:0];
    G = pixel_in[15:8];
    B = pixel_in[23:16];
    end
    
    wire[24:0] res_m0R;
    wire[24:0] res_m0G;
    wire[24:0] res_m0B;
    
    wire[24:0] res_m1R;
    wire[24:0] res_m1G;
    wire[24:0] res_m1B;
    
    wire[24:0] res_m2R;
    wire[24:0] res_m2G;
    wire[24:0] res_m2B;
    ///////////////////////////
    //pierwszy wiersz
    //////////////////////////
    mnozenie m00_R(
        .CLK(clk),
        .A(R),
        .B(matrix_00),
        .P(res_m0R) 
    );
    mnozenie m01_G(
        .CLK(clk),
        .A(G),
        .B(matrix_01),
        .P(res_m0G) 
    );
    mnozenie m02_B(
        .CLK(clk),
        .A(B),
        .B(matrix_10),
        .P(res_m0B) );
    ///////////////////////////
    //drugi wiersz
    //////////////////////////    
    mnozenie m10_R(
        .CLK(clk),
        .A(R),
        .B(matrix_10),
        .P(res_m1R) );
    mnozenie m11_G(
        .CLK(clk),
        .A(G),
        .B(matrix_11),
        .P(res_m1G) );
    mnozenie m12_B(
        .CLK(clk),
        .A(B),
        .B(matrix_12),
        .P(res_m1B) );
    ///////////////////////////
    //trzeci wiersz
    //////////////////////////
    mnozenie m20_R(
        .CLK(clk),
        .A(R),
        .B(matrix_20),
        .P(res_m2R) );
    mnozenie m21_G(
        .CLK(clk),
        .A(G),
        .B(matrix_21),
        .P(res_m2G) );
    mnozenie m22_B(
        .CLK(clk),
        .A(B),
        .B(matrix_22),
        .P(res_m2B) );
    ///////////////////////////
    //sumowanie R,G wiersz
    //////////////////////////
    
    wire[25:0] RG1;
    wire[25:0] RG2;
    wire[25:0] RG3;
    wire[25:0] BC1;
    wire[25:0] BC2;
    wire[25:0] BC3;
    reg[7:0] const_1 = 26'b0;
    reg[7:0] const_2 = {9'b010000000,17'b0};
    reg[7:0] const_3 = {9'b010000000,17'b0};
    
    wire[25:0] sumY;
    wire[25:0] sumCb;
    wire[25:0] sumCr;
    
    dodawanie rgY(
        .CLK(clk),
        .A(res_m0R),
        .B(res_m0G),
        .S(RG1));
    dodawanie bconstY(
        .CLK(clk),
        .A(res_m0B),
        .B(const_1),
        .S(BC1));
    dodawanie rgCr(
        .CLK(clk),
        .A(res_m1R),
        .B(res_m1G),
        .S(RG2));
    dodawanie bconstCr(
        .CLK(clk),
        .A(res_m1B),
        .B(const_1),
        .S(BC2));
    dodawanie rgCb(
        .CLK(clk),
        .A(res_m2R),
        .B(res_m2G),
        .S(RG3));
    dodawanie bconstCb(
        .CLK(clk),
        .A(res_m2B),
        .B(const_2),
        .S(BC3));
    
    ///////////////////////////
    //sumowanie RG, B wiersz
    //////////////////////////
    
    dodawanie sum_Y(
        .CLK(clk),
        .A(RG1),
        .B(BC1),
        .S(sumY));
    dodawanie sum_Cr(
        .CLK(clk),
        .A(RG2),
        .B(BC2),
        .S(sumCr));
    dodawanie sum_Cb(
        .CLK(clk),
        .A(RG3),
        .B(BC3),
        .S(sumCb));
    
    assign pixel_out[7:0] = sumY[25:18];
    assign pixel_out[15:8] = sumCr[25:18];
    assign pixel_out[23:16] = sumCb[25:18];
    
    wire del_de;
    wire del_hsync;
    wire del_vsync;
    
    ////////////////////////////////////////
    //opóŸnianie sygna³ów synchronizuj¹cych
    ///////////////////////////////////////
    
    Delayer#
        (.N(9)) 
    delay_de(
        .in(de_in),
        .out(del_de),
        .clk(clk)
    ); 
    
    Delayer#
        (.N(9)) 
    delay_vsync(
        .in(v_sync_in),
        .out(del_vsync),
        .clk(clk)); 
    
    
    Delayer #
        (.N(9)) 
    delay_hsync(
        .in(h_sync_in),
        .out(del_hsync),
        .clk(clk)
        ); 
        
    assign de_out = del_de;
    assign v_sync_out = del_vsync ;
    assign h_sync_out = del_hsync;
    
endmodule
