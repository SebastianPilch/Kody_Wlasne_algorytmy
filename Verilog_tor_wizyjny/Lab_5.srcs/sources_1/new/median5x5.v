`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 24.05.2023 09:33:10
// Design Name: 
// Module Name: median5x5
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


module median5x5
#(
    parameter H_SIZE = 83
//    parameter IMG_W = 64,
//    parameter IMG_H = 64
)

(
    input clk,
    input de,
    input vsync,
    input hsync,
    input[23:0] pixel_in,
    
    output de_out,
    output v_sync_out,
    output h_sync_out,
    output[23:0] pixel_out
    );
    
    reg[3:0] data;
    wire[15:0] WP_out;
    
    reg rst=0;
    reg ce = 1;
    reg[3:0]D11;
    reg[3:0]D12;
    reg[3:0]D13;
    reg[3:0]D14;
    reg[3:0]D15;
    reg[3:0]D21;
    reg[3:0]D22;
    reg[3:0]D23;
    reg[3:0]D24;
    reg[3:0]D25;
    reg[3:0]D31;
    reg[3:0]D32;
    reg[3:0]D33;
    reg[3:0]D34;
    reg[3:0]D35;
    reg[3:0]D41;
    reg[3:0]D42;
    reg[3:0]D43;
    reg[3:0]D44;
    reg[3:0]D45;
    reg[3:0]D51;
    reg[3:0]D52;
    reg[3:0]D53;
    reg[3:0]D54;
    reg[3:0]D55;   
    reg[4:0] sum = 0;
    reg context_valid;
    reg flag_v = 0;
    reg flag_h = 0;
    reg[23:0] new_color;
    reg[23:0] old_color;
    wire[23:0] del_old_color;
    reg eof;
    reg p_vsync;
    reg[11:0] pos_x = 1;
    reg[11:0] pos_y = 1;
    
    
//    reg[3:0] frame[4:0][4:0];    
//    reg[3:0] line[3:0];
//    generate 
//    genvar i;
//    genvar j;
//    for(i=0; i < 5; i = i+1)begin
//         for(j=0; j < 5; j = j+1)begin
//            always @(posedge clk) begin
//                frame[i][j] <= frame[i][j-1];
//            end
//         end
//    end
    

    always @(posedge clk)
    begin
        p_vsync <= D55[0];
        
        data = {pixel_in[0],de,hsync,vsync};
        D11 <= data;
        D12 <= D11;
        D13 <= D12;
        D14 <= D13;
        D15 <= D14;
        
        D21 <= WP_out[15:12];
        D22 <= D21;
        D23 <= D22;
        D24 <= D23;
        D25 <= D24;
        
        D31 <= WP_out[11:8];
        D32 <= D31;
        D33 <= D32;
        D34 <= D33;
        D35 <= D34;
        
        D41 <= WP_out[7:4];
        D42 <= D41;
        D43 <= D42;
        D44 <= D43;
        D45 <= D44;
        
        D51 <= WP_out[3:0];
        D52 <= D51;
        D53 <= D52;
        D54 <= D53;
        D55 <= D54;
        
        
        if (D33[2]) begin
        sum = D11[3] + D12[3] + D13[3] + D14[3] + D15[3] + D21[3] + D22[3] + D23[3] + D24[3] + D25[3]+ D31[3] + D32[3] + D33[3] + D34[3] + D35[3]+ D41[3] + D42[3] + D43[3] + D44[3] + D45[3]+ D51[3] + D52[3] + D53[3] + D54[3] + D55[3];
        new_color = (sum > 5'd12) ? 24'hffffff : 24'h000000;
        context_valid = D33[2];
        end else begin        
        new_color = (D33[3] == 1) ? 24'hffffff : 24'h000000;
        context_valid = D33[2];
        end  
        flag_h = D33[1];
        flag_v <= D33[0];
    end

    delayLinieBRAM_WP Wp0(
        .clk(clk),
        .rst(rst),
        .ce(ce),
        .h_size(H_SIZE-5),
        .din({D15,D25,D35,D45}),
        .dout(WP_out)
        
    );

    

    assign pixel_out = new_color;
    assign v_sync_out = flag_v;
    assign h_sync_out = flag_h;
    assign de_out = context_valid;
    

endmodule
