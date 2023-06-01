`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 27.04.2023 10:11:15
// Design Name: 
// Module Name: tb_posxy
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


module tb_posxy(

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
	 


wire mask ;
assign mask = rx_red[0];
wire[11:0]x1;
wire[11:0]y1;
wire[11:0]x2;
wire[11:0]y2;
wire[11:0]x;
wire[11:0]y;
wire vis_vsync;
wire vis_hsync;
wire vis_de;
wire[7:0] vis_R;
wire[7:0] vis_G;
wire[7:0]vis_B;

cetroid_rectangle
    cen(
    .clk(rx_pclk),
    .de(rx_de),
    .hsync(rx_hsync),
    .vsync(rx_vsync),
    .mask(mask),
    .x1(x1),
    .x2(x2),
    .y1(y1),
    .y2(y2)
);
//centroid #(
//    .IMG_H(64), 
//    .IMG_W(64)
//    )
//    cen(
//    .clk(rx_pclk),
//    .de(rx_de),
//    .hsync(rx_hsync),
//    .vsync(rx_vsync),
//    .mask(mask),
//    .x(x),
//    .y(y)

//);


//vis_centroid#(
//    .IMG_H(64), 
//    .IMG_W(64)
//    ) viscen(
//    .clk(rx_pclk),
//    .de(rx_de),
//    .hsync(rx_hsync),
//    .vsync(rx_vsync),
//    .x(x),
//    .y(y), 
//    .pixel_in({rx_red,rx_green,rx_blue}),
//    .pixel_out({vis_R,vis_G,vis_B}),
//    .hsync_out(vis_hsync),
//    .vsync_out(vis_vsync),
//    .de_out(vis_de)
//);
vis_rectangle vis(
    .clk(rx_pclk),
    .de(rx_de),
    .hsync(rx_hsync),
    .vsync(rx_vsync),
    .x1(x1),
    .y1(y1),
    .x2(x2),
    .y2(y2), 
    .pixel_in({rx_red,rx_green,rx_blue}),
    .pixel_out({vis_R,vis_G,vis_B}),
    .hsync_out(vis_hsync),
    .vsync_out(vis_vsync),
    .de_out(vis_de)
);

hdmi_out64 outfile(
  .hdmi_clk(rx_pclk),
  .hdmi_vs(vis_vsync),
  .hdmi_de(vis_de),
  .hdmi_data({8'b0,vis_R,vis_G,vis_B})
);
endmodule
