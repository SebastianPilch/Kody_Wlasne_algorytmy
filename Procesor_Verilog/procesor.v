`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 15.06.2023 11:05:41
// Design Name: 
// Module Name: procesor
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


module procesor(
        input clk,
        input[7:0] gpi,
        output[7:0] gpo
    );
    

    reg[7:0] Rejestry_wewnetrzne[7:0];
    wire[7:0]suma;
    
    initial begin
        Rejestry_wewnetrzne[0] = 0;
        Rejestry_wewnetrzne[1] = 5;
        Rejestry_wewnetrzne[2] = 0;
        Rejestry_wewnetrzne[3] = 0;
        Rejestry_wewnetrzne[4] = 0;
        Rejestry_wewnetrzne[5] = 0;
        Rejestry_wewnetrzne[6] = 0;
        Rejestry_wewnetrzne[7] = 0;
    end

    wire[31:0] instr;
    wire[1:0] pc_op;
    wire[1:0] alu_op;
    wire[2:0] rx_op;
    wire imm_op;
    wire[2:0] ry_op;
    wire rd_op;
    wire[2:0] d_op;
    wire[7:0] imm;
    wire[7:0] save_con;
    wire[7:0]data_to_save_in_reg;
    wire[7:0]alu_res;
    wire[7:0]mem_data;
    wire[7:0]x;
    wire[7:0]y;
    wire[7:0]ostateczny_y;
    wire[7:0]ostateczny_Y;
    wire[7:0]iloczyn_logiczny;
    wire zero;

    assign pc_op = instr[25:24];
    assign alu_op = instr[21:20];
    assign rx_op = instr[18:16];
    assign imm_op = instr[15];
    assign ry_op = instr[14:12];
    assign rd_op = instr[11];
    assign d_op = instr[10:8];
    assign imm = instr[7:0];
    assign gpo =Rejestry_wewnetrzne[5] ;
    
    d_mem dane(
        .address(alu_res),
        .data(mem_data)
    );  
    i_mem instrukcje(
        .address(Rejestry_wewnetrzne[7]),
        .data(instr)
    );
    
    dekoder dekoder_rejestrow(
    .address(d_op),
    .out(save_con)
    ); 
    
    mux8_1 rd_mux(
    .R0(alu_res),
    .R1(mem_data),
    .adres({2'b00,rd_op}),
    .out(data_to_save_in_reg)
    );
    
    mux8_1 pc_mux(
    .R0(alu_res),
    .R1(Rejestry_wewnetrzne[7]+1),
    .adres({2'b00,jmp}),
    .out(nowy_pcr7)
    );
    mux8_1 rx_mux(
    .R0(Rejestry_wewnetrzne[0]),
    .R1(Rejestry_wewnetrzne[1]),
    .R2(Rejestry_wewnetrzne[2]),
    .R3(Rejestry_wewnetrzne[3]),
    .R4(Rejestry_wewnetrzne[4]),
    .R5(Rejestry_wewnetrzne[5]),
    .R6(Rejestry_wewnetrzne[6]),
    .R7(Rejestry_wewnetrzne[7]),
    .adres(rx_op),
    .out(x)
    );
    
    mux8_1 ry_mux(
    .R0(Rejestry_wewnetrzne[0]),
    .R1(Rejestry_wewnetrzne[1]),
    .R2(Rejestry_wewnetrzne[2]),
    .R3(Rejestry_wewnetrzne[3]),
    .R4(Rejestry_wewnetrzne[4]),
    .R5(Rejestry_wewnetrzne[5]),
    .R6(Rejestry_wewnetrzne[6]),
    .R7(Rejestry_wewnetrzne[7]),
    .adres(ry_op),
    .out(y));

mux8_1 imm_mux(
    .R0(y),
    .R1(imm),
    .adres({2'b00,imm_op}),
    .out(ostateczny_y)
    );
    
    ALU ALU(
    .rx(x),
    .ry(ostateczny_y),
    .sum_out(suma),
    .and_out(iloczyn_logiczny),
    .zero_con(zero)
    );
    
    mux8_1 alu_mux(
    .R0(iloczyn_logiczny),
    .R1(suma),
    .R2({zero,7'b0000000}),
    .R3(ostateczny_y),
    .adres({1'b0,alu_op}),
    .out(alu_res)
    );
    
    warunek_skoku jmp_blok
    (
    .rodzaj_skoku(pc_op),
    .zero_con(zero),
    .skok(jmp)
    );
    
    always @(posedge clk) begin
        Rejestry_wewnetrzne[4] = gpi;
        if(save_con[0])begin Rejestry_wewnetrzne[0] = data_to_save_in_reg; end
        if(save_con[1])begin Rejestry_wewnetrzne[1] = data_to_save_in_reg; end    
        if(save_con[2])begin Rejestry_wewnetrzne[2] = data_to_save_in_reg; end    
        if(save_con[3])begin Rejestry_wewnetrzne[3] = data_to_save_in_reg; end    
        if(save_con[4])begin Rejestry_wewnetrzne[4] = data_to_save_in_reg; end    
        if(save_con[5])begin Rejestry_wewnetrzne[5] = data_to_save_in_reg; end     
        if(jmp)begin 
            Rejestry_wewnetrzne[7] = alu_res; 
        end else begin 
            Rejestry_wewnetrzne[7] = Rejestry_wewnetrzne[7]+1 ;
        end

    
    end
     
endmodule
