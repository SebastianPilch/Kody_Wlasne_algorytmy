`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 24.05.2023 12:50:22
// Design Name: 
// Module Name: tb_mediana
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


module tb_mediana(

    );
    
    wire rx_pclk;
wire rx_de;
wire rx_hsync;
wire rx_vsync;
wire [7:0] rx_red;
wire [7:0] rx_green;
wire [7:0] rx_blue;



    
    // --------------------------------------
// HDMI input
// --------------------------------------
hdmi_in64 file_input (
    .hdmi_clk(rx_pclk), 
    .hdmi_de(rx_de), 
    .hdmi_hs(rx_hsync), 
    .hdmi_vs(rx_vsync), 
    .hdmi_r(rx_red), 
    .hdmi_g(rx_green), 
    .hdmi_b(rx_blue)
    );
    
wire med_de;
wire med_hsync;
wire med_vsync;
wire [23:0] med_pixel;

    
Sobel 
#(
    .H_SIZE(83)
    
)
filtr(

    .clk(rx_pclk),
    .de(rx_de),
    .vsync(rx_vsync),
    .hsync(rx_hsync),
    .pixel_in({rx_red,rx_green,rx_blue}),
    
    .de_out(med_de),
    .v_sync_out(med_vsync),
    .h_sync_out(med_hsync),
    .pixel_out(med_pixel)
    );

    
 hdmi_out64 outfile(
  .hdmi_clk(rx_pclk),
  .hdmi_vs(med_vsync),
  .hdmi_de(med_de),
  .hdmi_data({8'b0,med_pixel})
);   
    
endmodule
