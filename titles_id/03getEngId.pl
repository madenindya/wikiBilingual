#!/usr/local/bin/perl

open (IN, "en_id_title_result");
open (OUT, ">en_ids");

my $line = <IN>;
my $prev_id;
while ($line = <IN>) {
	chop($line);

	my @tokens = split(/\//, $line);
	if ($prev_id != $tokens[0]) {
		print OUT "$tokens[0]\n";
	}

	$prev_id = $tokens[0];
}

close(IN);
close(OUT);