import socketserver

import bidding

from lstm_bidder import Bidder
from correspondence import parse_line, bid_to_jack_format


bidder = Bidder('bw5c', './bw5c_model/bw5c-500000')


def add_next_bid(line):
    _, deal_data = parse_line(line)

    if bidding.auction_over(deal_data.auction):
        return line

    bid = bidder.next_bid(deal_data, deal_data.auction)

    return line + bid_to_jack_format(bid)


class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        self.data = self.rfile.readline().strip().decode('ascii')
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        response = add_next_bid(self.data)

        self.wfile.write((response + '\n').encode('ascii'))

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8427

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('bye')
    finally:
        server.shutdown()
