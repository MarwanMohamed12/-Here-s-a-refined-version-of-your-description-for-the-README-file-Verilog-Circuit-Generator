module adder_4bit_TB();
parameter n_TB =4 ;

reg clk_TB;
reg rst_TB;
reg [n-1:0] add1_TB;
reg [n-1:0] add2_TB;
reg carry_in_TB ;
wire [n-1:0] sum_TB;
wire carry_out_TB;

adder_4bit #(.n(n_TB)) dut (.clk(clk_TB),.rst(rst_TB),.add1(add1_TB),.add2(add2_TB),.carry_in(carry_in_TB),.sum(sum_TB),.carry_out(carry_out_TB));

always #5 clk =~ clk ;

initial begin


end

endmodule