`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 17.05.2023 21:13:23
// Design Name: 
// Module Name: rgb2hsv
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


module rgb2hsv(
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
    
    reg[9:0] min;
    reg[9:0] V;
    wire signed[9:0] C;
    reg[1:0] posV;
    wire[1:0] posV_del;
    reg[1:0] posmin;
    wire signed[11:0] H_bef_check[2:0];
    reg[11:0] H_bef_check_out;
    wire signed[31:0] H_bef_const_sum[2:0];
    wire signed[11:0] H_checked_sum;
    wire signed[11:0] H_checked_sum_without360;
    wire [9:0] fractional_RGB[2:0];
    reg[9:0] fractional_RGB_del[2:0];
    wire[9:0] color_diff_vector[2:0];
    wire signed [23:0] final_S_div;
    reg signed[9:0] color_diff_vector_del[2:0];
    wire signed[23:0] final_H_div;
    reg signed[7:0] final_H;
    wire signed[17:0] mult60[2:0];
    reg signed[17:0] mult60_del[2:0];
    wire[17:0]final_S;
    wire[17:0]final_V;
    reg[7:0] V_to_pixel;
    wire[7:0] delayed_final_S;
    wire[7:0] delayed_final_V;
    reg[7:0] S_to_pixel;
    reg[7:0] H_to_pixel;
    wire[2:0] sync_signals_del;
    
    assign fractional_RGB[0][9] = 1'b0;
    assign fractional_RGB[1][9] = 1'b0;
    assign fractional_RGB[2][9] = 1'b0;
    
    always @(posedge clk)

    begin
        mult60_del[0] <= mult60[0];
        mult60_del[1] <= mult60[1];
        mult60_del[2] <= mult60[2];
        V_to_pixel <= delayed_final_V;
        color_diff_vector_del[0] <= color_diff_vector[0];
        color_diff_vector_del[1] <= color_diff_vector[1];
        color_diff_vector_del[2] <= color_diff_vector[2];
        
        fractional_RGB_del[0] <= fractional_RGB[0];
        fractional_RGB_del[1] <= fractional_RGB[1];
        fractional_RGB_del[2] <= fractional_RGB[2];
        
        if (fractional_RGB[2] > fractional_RGB[1] & fractional_RGB[2] > fractional_RGB[0])
        begin 
            posV = 2;
            V = fractional_RGB[2];
        end else if (fractional_RGB[1] > fractional_RGB[2] & fractional_RGB[1] > fractional_RGB[0]) begin
            posV = 1;
            V = fractional_RGB[1];        
        end else begin
            posV = 0;
            V = fractional_RGB[0];   
        if (V == 0) begin posV = 3; end
            
        end
        
        if (fractional_RGB[2] < fractional_RGB[1] & fractional_RGB[2] < fractional_RGB[0])
        begin 
            posmin = 2;
            min = fractional_RGB[2];
        end else if (fractional_RGB[1] < fractional_RGB[2] & fractional_RGB[1] < fractional_RGB[0]) begin
            posmin = 1;
            min = fractional_RGB[1];        
        end else begin
            posmin = 0;
            min = fractional_RGB[0];   
        end
        
    case(posV_del) 
    2'b00:
        H_bef_check_out = H_bef_check[0]; 
    2'b01:
        H_bef_check_out = H_bef_check[1];
    2'b10:
        H_bef_check_out = H_bef_check[2];
    2'b11:
        H_bef_check_out = 11'sd0;
    endcase
    
    if(delayed_final_V == 0)begin
        S_to_pixel = 0;
    end else begin
        S_to_pixel = delayed_final_S;
    end 
    
    H_to_pixel <= {1'b0, final_H[7:1]};
    if(H_bef_check_out[11] == 0) begin 
        final_H = H_checked_sum_without360[7:0];
    end else begin
        final_H = final_H_div[15:8];
    end
    
    end    
    //////
    // delay line
    //////
    
    Delayer#(
    .N(12),
    .DELAY(24)
    ) 
    finalne (
    .clk(clk),
    .in(H_bef_check_out),
    .out(H_checked_sum_without360)
    
    );
    
    Delayer#(
    .N(3),
    .DELAY(75)
    ) 
    synchronizacja (
    .clk(clk),
    .in({v_sync_in,h_sync_in,de_in}),
    .out(sync_signals_del)
    
    );
    
    
    Delayer#(
    .N(2),
    .DELAY(29)
    ) 
    przeuniecie_warunku_V (
    .clk(clk),
    .in(posV),
    .out(posV_del)
    );
    
    
    Delayer#(
    .N(8),
    .DELAY(55)
    ) 
    przeuniecie_finalnegoV (
    .clk(clk),
    .in(final_V[15:8]),
    .out(delayed_final_V)
    );
    
    Delayer#(
    .N(8),
    .DELAY(33)
    ) 
    przeuniecie_finalnego_S (
    .clk(clk),
    .in(final_S[15:8]),
    .out(delayed_final_S)
    );
     ///////
    
    /// dzielnik 255
    
    ////////
    dzielnik_na_255 do01R(
        .s_axis_dividend_tdata(pixel_in[23:16]),
        .s_axis_divisor_tdata(8'hff),
        .aclk(clk),
        .m_axis_dout_tdata(fractional_RGB[0][8:0])
    );
    dzielnik_na_255 do01G(
        .s_axis_dividend_tdata(pixel_in[15:8]),
        .s_axis_divisor_tdata(8'hff),
        .aclk(clk),
        .m_axis_dout_tdata(fractional_RGB[1][8:0])
    );
    dzielnik_na_255 do01B(
        .s_axis_dividend_tdata(pixel_in[7:0]),
        .s_axis_divisor_tdata(8'hff),
        .aclk(clk),
        .m_axis_dout_tdata(fractional_RGB[2][8:0])
    );
    ///////
    
    /// odejmowania
    
    ////////
    
    color_diffrence diffGB(
    .A(fractional_RGB[1]),
    .B(fractional_RGB[2]),
    .S(color_diff_vector[0])
    );
    color_diffrence diffBR(
    .A(fractional_RGB[2]),
    .B(fractional_RGB[0]),
    .S(color_diff_vector[1])
    );
    color_diffrence diffRG(
    .A(fractional_RGB[0]),
    .B(fractional_RGB[1]),
    .S(color_diff_vector[2])    
    );
    
    color_diffrence VC(
    .A(V),
    .B(min),
    .S(C)  
    );
     ///////
    
    /// sumatory
    
    ////////
    sum_0_120_240_360 stala0(
    .A(H_bef_const_sum[0][19:8]),
    .B(12'sd0),
    .S(H_bef_check[0])
    );
    sum_0_120_240_360 stala120(
    .A(H_bef_const_sum[1][19:8]),
    .B(12'sd120),
    .S(H_bef_check[1])
    );
    sum_0_120_240_360 stala240(
    .A(H_bef_const_sum[2][19:8]),
    .B(12'sd240),
    .S(H_bef_check[2])
    );
    
    sum_0_120_240_360 stala360(
    .A(H_bef_check_out),
    .B(12'sd360),
    .S(H_checked_sum)
    );
    ///////
    
    /// dzielarka 360
    
    ////////
    
    dzielnik_na_360 dzielH(
    .s_axis_dividend_tdata(H_checked_sum),
    .s_axis_divisor_tdata(12'sd360),
    .aclk(clk),
    .m_axis_dout_tdata(final_H_div)
    );
    //////
    // Dzielenie S
    /////
    
    div_S finalna_wartoscS(
    .s_axis_dividend_tdata(C),
    .s_axis_divisor_tdata(V),
    .aclk(clk),
    .m_axis_dout_tdata(final_S_div)
    );
    
    
    
    ///////
    
    /// mnozarki razy 60
    
    ////////
    mult_gen_1 V_R60(
    .A(color_diff_vector[0]),
    .B(8'sd60),
    .P(mult60[0])
    );
    
    mult_gen_1 V_G60(
    .A(color_diff_vector[1]),
    .B(8'sd60),
    .P(mult60[1])
    );
    mult_gen_1 V_B60(
    .A(color_diff_vector[1]),
    .B(8'sd60),
    .P(mult60[2])
    );
    
    ///////
    
    /// dzielarka na C
    
    ////////
    
    DivC DivforR
    (
    .s_axis_dividend_tdata(mult60_del[0]),
    .s_axis_divisor_tdata(C),
    .aclk(clk),
    .m_axis_dout_tdata(H_bef_const_sum[0])
    
    
    );
    DivC DivforG
    (
    .s_axis_dividend_tdata(mult60_del[1]),
    .s_axis_divisor_tdata(C),
    .aclk(clk),
    .m_axis_dout_tdata(H_bef_const_sum[1])
    
    
    );      
    DivC DivforB
    (
    .s_axis_dividend_tdata(mult60_del[2]),
    .s_axis_divisor_tdata(C),
    .aclk(clk),
    .m_axis_dout_tdata(H_bef_const_sum[2])
    
    );    
    

    ////////
    // Wyjœcia mno¿enie * 255
    ///////
    mnozarka255 V_wyj(
        .A(V),
        .B(8'hff),
        .P(final_V)
    );
    
    mnozarka255 S_wyj(
        .A(final_S_div[9:0]),
        .B(8'hff),
        .P(final_S)
    );
    
    assign pixel_out = {H_to_pixel,S_to_pixel,V_to_pixel};
    assign v_sync_out = sync_signals_del[2];
    assign h_sync_out = sync_signals_del[1];
    assign de_out = sync_signals_del[0];
endmodule
