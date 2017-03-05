#!/usr/local/bin/perl

open(IN, "enwiki-20170220-page.sql");
open(OUT, ">tmp-enwiki-20170220-page");

my $line;

print OUT ("id/title\n");

print "Start\n";
while ($line = <IN>) {
	chop($line);

	if ($line =~ /INSERT INTO/) {

		$line =~ s/INSERT INTO .* VALUES //;
		$line =~ s/;$//;

		my @tokens = split(/\)\,\(/, $line);

		for my $token (@tokens) {
			$token =~ s/^\(//;
			$token =~ s/\)$//;
			
			my @tokenz = split(/\,/, $token);

			my $title = $tokenz[2];
			$title =~ s/^\'//;
			$title =~ s/\'$//;
			$title =~ s/\_/ /g;

			print OUT "$tokenz[0]###$title\n";
		}
	}
}

print "End\n";

close(IN);
close(OUT);