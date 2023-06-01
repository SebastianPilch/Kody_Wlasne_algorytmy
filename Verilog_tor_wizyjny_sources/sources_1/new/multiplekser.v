`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 12.04.2023 17:15:17
// Design Name: 
// Module Name: multiplekser
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


module multiplekser(
    input de_in_ycrcb,
    input v_sync_in_ycrcb,
    input h_sync_in_ycrcb,
    input[23:0] pixel_in_ycrcb,
    input de_in_ycrcb_bin,
    input v_sync_in_ycrcb_bin,
    input h_sync_in_ycrcb_bin,
    input[23:0] pixel_in_ycrcb_bin,
    input de_in_vp_brak,
    input v_sync_in_vp_brak,
    input h_sync_in_vp_brak,
    input[23:0] pixel_in_vp_brak,
    input de_in_vp_lut,
    input v_sync_in_vp_lut,
    input h_sync_in_vp_lut,
    input[23:0] pixel_in_vp_lut,
    input de_in_vp_bin,
    input v_sync_in_vp_bin,
    input h_sync_in_vp_bin,
    input[23:0] pixel_in_vp_bin,
    input de_in_cent,
    input v_sync_in_cent,
    input h_sync_in_cent,
    input[23:0] pixel_in_cent,
    input de_in_cent_kolo,
    input v_sync_in_cent_kolo,
    input h_sync_in_cent_kolo,
    input[23:0] pixel_in_cent_kolo,
    input de_in_cent_rect,
    input v_sync_in_cent_rect,
    input h_sync_in_cent_rect,
    input[23:0] pixel_in_cent_rect,
    input de_in_filter,
    input v_sync_in_filter,
    input h_sync_in_filter,
    input[23:0] pixel_in_filter,
    input de_in_srednia,
    input v_sync_in_srednia,
    input h_sync_in_srednia,
    input[23:0] pixel_in_srednia,
    input de_in_Sobel,
    input v_sync_in_Sobel,
    input h_sync_in_Sobel,
    input[23:0] pixel_in_Sobel,
        input de_in_hsv,
    input v_sync_in_hsv,
    input h_sync_in_hsv,
    input[23:0] pixel_in_hsv,
        input de_in_erozja,
    input v_sync_in_erozja,
    input h_sync_in_erozja,
    input[23:0] pixel_in_erozja,
    input[3:0] adres,
    input clk,
    output de_out,
    output v_sync_out,
    output h_sync_out,
    output[23:0] pixel_out
    );
   reg[3:0]ADRES0 = 4'b0000 ;
   reg[3:0]ADRES1 = 4'b0001 ;
   reg[3:0]ADRES2 = 4'b0010 ;
   reg[3:0]ADRES3 = 4'b0011 ;
   reg[3:0]ADRES4 = 4'b0100 ;
   reg[3:0]ADRES5 = 4'b0101 ;
   reg[3:0]ADRES6 = 4'b0110 ;
   reg[3:0]ADRES7 = 4'b0111 ;
   reg[3:0]ADRES8 = 4'b1000 ;
   reg[3:0]ADRES9 = 4'b1010 ;
   reg[3:0]ADRES10 = 4'b1001 ;
   reg[3:0]ADRES11 = 4'b1011 ;
   reg[3:0]ADRES12 = 4'b1111 ;
   reg v_sync=0;
   reg h_sync=0;
   reg de=0;
   reg[23:0] pixel;
   reg[3:0] address;

   always @(posedge clk) begin
   address <= adres;
   case (address)
       ADRES0:
        begin
            pixel = pixel_in_vp_brak;
            v_sync = v_sync_in_vp_brak;
            h_sync = h_sync_in_vp_brak;
            de = de_in_vp_brak;
       end
       ADRES1:
       begin
            pixel = pixel_in_vp_lut;
            v_sync = v_sync_in_vp_lut;
            h_sync = h_sync_in_vp_lut;
            de = de_in_vp_lut;
       end
       ADRES2:
       begin
            pixel = pixel_in_vp_bin;
            v_sync = v_sync_in_vp_bin;
            h_sync = h_sync_in_vp_bin;
            de = de_in_vp_lut;
       end
       ADRES3:
       begin
            pixel = pixel_in_ycrcb;
            v_sync = v_sync_in_ycrcb;
            h_sync = h_sync_in_ycrcb;
            de = de_in_ycrcb;
       end
       ADRES4:
       begin
            pixel = pixel_in_ycrcb_bin;
            v_sync = v_sync_in_ycrcb_bin;
            h_sync = h_sync_in_ycrcb_bin;
            de = de_in_ycrcb_bin;
       end
       ADRES5:
       begin
            pixel = pixel_in_cent;
            v_sync = v_sync_in_cent;
            h_sync = h_sync_in_cent;
            de = de_in_cent;
       end
       ADRES6:
       begin
            pixel = pixel_in_cent_kolo;
            v_sync = v_sync_in_cent_kolo;
            h_sync = h_sync_in_cent_kolo;
            de = de_in_cent_kolo;
       end
       ADRES7:
       begin
            pixel = pixel_in_cent_rect;
            v_sync = v_sync_in_cent_rect;
            h_sync = h_sync_in_cent_rect;
            de = de_in_cent_rect;
       end
       
       ADRES8:
       begin
            pixel = pixel_in_filter;
            v_sync = v_sync_in_filter;
            h_sync = h_sync_in_filter;
            de = de_in_filter;
       end
      ADRES9:
       begin
            pixel = pixel_in_srednia;
            v_sync = v_sync_in_srednia;
            h_sync = h_sync_in_srednia;
            de = de_in_srednia;
       end
      ADRES10:
       begin
            pixel = pixel_in_Sobel;
            v_sync = v_sync_in_Sobel;
            h_sync = h_sync_in_Sobel;
            de = de_in_Sobel;
       end
             ADRES11:
       begin
            pixel = pixel_in_hsv;
            v_sync = v_sync_in_hsv;
            h_sync = h_sync_in_hsv;
            de = de_in_hsv;
       end
             ADRES12:
       begin
            pixel = pixel_in_erozja;
            v_sync = v_sync_in_erozja;
            h_sync = h_sync_in_erozja;
            de = de_in_erozja;
       end
    endcase
    end
    assign de_out = de;
    assign v_sync_out = v_sync;
    assign h_sync_out= h_sync;
    assign pixel_out = pixel;

endmodule
